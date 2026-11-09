---
symbol: "PLXNA2"
type: "gene"
col: 1151
ensembl_id: "ENSG00000076356"
name: "plexin A2"
location: "1q32.2"
module: 147
arm: "+"
pooled_cpm: 26.7
n_lines_expressing: 35
n_dd_up: 24
n_dd_down: 13
n_dd_up_clean: 19
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 10
direction_downstream: 20
tags: ["gene", "module/147"]
generated_by: "tahoemap"
---

# PLXNA2

*plexin A2* — 1q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.05 µM: 1.88× (z +6.0, q 2e-06, up in 14 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.5 µM: 0.507× (z -7.8, q 3e-12, down in 25 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MICAL2]] (+0.58, fdr 1e-05), [[NES]] (+0.55, fdr 1e-05), [[MAP4K4]] (+0.55, fdr 1e-05); moves opposite to [[TMEM144]] (-0.52, fdr 1e-05), [[PREPL]] (-0.49, fdr 2e-05), [[CNNM2]] (-0.48, fdr 3e-05).
> It is in [[Module 147]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[CSPG4]] → it (grade B ⚠); 20 go from it, the strongest it → [[ACOT7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1151.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **1.88×** | +6.0 | 2e-06 | 14/33 (LS 180, A549, …) | inconsistent across doses | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +5.5 | 9e-06 | 13/32 (NCI-H1792, SW 900, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +5.3 | 2e-05 | 17/33 (A498, NCI-H1573, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +5.0 | 7e-05 | 12/33 (LS 180, RKO, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.32×** | +4.5 | 6e-04 | 11/33 (AN3 CA, A549, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **2.09×** | +4.4 | 9e-04 | 9/33 (LoVo, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.70×** | +4.4 | 1e-03 | 7/28 (LOX-IMVI, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.51×** | +4.3 | 0.001 | 7/27 (RPMI-7951, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +3.9 | 0.005 | 11/30 (RKO, LoVo, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Demeclocycline (drug)]] 5 µM |  | **1.27×** | +3.9 | 0.006 | 13/33 (SHP-77, NCI-H2347, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | **1.27×** | +3.8 | 0.007 | 11/33 (HepG2/C3A, J82, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.38×** | +3.7 | 0.011 | 13/33 (C32, HT-29, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.39×** | +3.6 | 0.012 | 8/23 (LOX-IMVI, SW 900, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.41×** | +3.6 | 0.013 | 13/31 (NCI-H2347, NCI-H1792, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.031 | 11/32 (NCI-H1573, NCI-H2347, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.33×** | +3.2 | 0.043 | 11/33 (A-172, HS-578T, …) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.045 | 9/33 (LoVo, J82, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.045 | 10/32 (NCI-H1573, SHP-77, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.39×** | +3.1 | 0.051 | 13/31 (NCI-H2347, H4, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1151.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM |  | **0.507×** | -7.8 | 3e-12 | 25/31 (J82, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.667×** | -6.6 | 1e-08 | 21/33 (J82, A-172, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.599×** | -5.9 | 7e-07 | 21/33 (HOP62, J82, …) | top dose only | cell-cycle shift (explains ~8% here); composition shift |
| [[Radotinib (drug)]] 5 µM |  | **0.715×** | -5.5 | 6e-06 | 19/33 (SHP-77, HOP62, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.633×** | -5.3 | 2e-05 | 19/31 (SNU-1, HOP62, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **0.660×** | -4.8 | 2e-04 | 14/33 (HS-578T, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.504×** | -4.1 | 0.003 | 13/29 (A-172, J82, …) | top dose only | cell-cycle shift (explains ~25% here); noisy plate (z scaled) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **0.712×** | -3.8 | 0.012 | 12/32 (SNU-1, HOP62, …) | rises with dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.723×** | -3.7 | 0.012 | 16/32 (hTERT-HPNE, HOP62, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM |  | **0.786×** | -3.6 | 0.018 | 15/33 (SHP-77, J82, …) | rises with dose | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.746×** | -3.3 | 0.059 | 16/31 (A-172, HOP62, …) | rises with dose | composition shift |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **0.754×** | -3.1 | 0.081 | 4/32 (HCT15, HS-578T, …) | top dose only | plate-row cell shift |
| [[Cobimetinib (drug)]] 0.05 µM |  | **0.747×** | -3.1 | 0.081 | 13/30 (SHP-77, RKO, …) | inconsistent across doses |  |
| [[Vandetanib (drug)]] 5 µM |  | 0.769× | -3.0 | 0.10 | 11/32 (BT-474, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1151. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 40.4 | 0 | 10 (8 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.406× (z -15.1) ⚠ position not correctable · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0968× (z -11.2) |
| [[SNU-1 (line)]] | wt | 94.3 | 0 | 8 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0834× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.254× (z -10.0) |
| [[A-172 (line)]] | wt | 185 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0549× (z -20.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.144× (z -9.7) |
| [[J82 (line)]] | alt | 46.0 | 0 | 5 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.188× (z -13.4) |
| [[Hs 766T (line)]] | wt | 186 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -13.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 52.5 | 0 | 3 | — | [[Binimetinib (drug)]] 5 µM 0.234× (z -9.7) |
| [[HS-578T (line)]] | alt | 18.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 93.9 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.297× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 40.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 6.88× (z +11.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Digitoxin (drug)]] 5 µM 0.177× (z -10.4) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 39.5 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.133× (z -9.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Selinexor (drug)]] 0.5 µM 0.158× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 32.3 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.104× (z -10.2) |
| [[KATO III (line)]] | alt | 35.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.247× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 44.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.317× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 17.5 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.498× (z -9.7) ⚠ position not correctable |
| [[A-427 (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.52 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.45 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.73 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.66 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.22 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.39 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.36 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.14 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.48 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.63 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.82 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1151), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MICAL2]] | +0.58 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[NES]] | +0.55 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[MAP4K4]] | +0.55 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[PLXNA1]] | +0.55 | +0.50 / +0.54 | both halves | 1e-05 | same gene group; pathway: CRMPs in Sema3A signaling; STRING 709 |
| [[GATAD2A]] | +0.54 | +0.46 / +0.60 | both halves | 3e-05 |  |
| [[ABLIM3]] | +0.54 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[SH3RF3]] | +0.53 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[ASAP2]] | +0.53 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[JAK2]] | +0.53 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[LTBP1]] | +0.52 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[CLMP]] | +0.52 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[KPNA4]] | +0.52 | +0.50 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM144]] | -0.52 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[PREPL]] | -0.49 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[CNNM2]] | -0.48 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[SLC11A2]] | -0.48 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[CFAP36]] | -0.48 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[CCNG2]] | -0.48 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[TNFAIP6]] | -0.47 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[RBPJ]] | -0.47 | -0.42 / -0.43 | both halves | 4e-05 | same gene group |
| [[C20orf96]] | -0.47 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[FHIP1A]] | -0.46 | -0.36 / -0.55 | both halves | 9e-05 |  |
| [[RAB9A]] | -0.46 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[TESMIN]] | -0.46 | -0.44 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CSPG4]] | B | CSPG4 activity weakens PLXNA2's drug response | lines that do not express CSPG4 (20) vs lines expressing it (13) | the lines without CSPG4 respond 0.97× as strongly (z diff +0.16); strongest at Tucidinostat 5 µM: 1.47x vs 1.02x (z diff -2.6) | 0.012 | ⚠ within organs, on part of the lines; also absent: MMP2, PCDH18, AEBP1; target measured in part of the lines; both ways; artifact flags |
| [[HIPK2]] | B | HIPK2 activity raises PLXNA2's level | lines that do not express HIPK2 (5) vs lines expressing it (45) | 4.84× lower at baseline in the lines without HIPK2 | 0.018 | ⚠ within organs, on part of the lines; also absent: MARCHF3, ASPH, ENSG00000286533; maybe low, not absent |
| [[PLAT]] | B | PLAT activity raises PLXNA2's level | lines that do not express PLAT (28) vs lines expressing it (22) | 2.14× lower at baseline in the lines without PLAT | 0.018 | ⚠ within organs, on part of the lines; also absent: TIMP3, FN1, SNAI2 |
| [[FN1]] | B | FN1 activity raises PLXNA2's level | lines that do not express FN1 (29) vs lines expressing it (21) | 2.38× lower at baseline in the lines without FN1 | 0.020 | ⚠ within organs, on part of the lines; also absent: PLPP4, ENSG00000234261, IL7R |
| [[TFCP2L1]] | B | TFCP2L1 activity lowers PLXNA2's level | lines that do not express TFCP2L1 (22) vs lines expressing it (28) | 2.06× higher at baseline in the lines without TFCP2L1 | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000267748, OCLN, SPINT2 |
| [[CSPG4]] | B | CSPG4 activity raises PLXNA2's level | lines that do not express CSPG4 (31) vs lines expressing it (19) | 1.91× lower at baseline in the lines without CSPG4 | 0.034 | ⚠ within organs, on part of the lines; also absent: MMP2, PCDH18, AEBP1 |
| [[ANPEP]] | B | ANPEP activity raises PLXNA2's level | lines that do not express ANPEP (33) vs lines expressing it (17) | 2.33× lower at baseline in the lines without ANPEP | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LINC01615, ENSG00000224865 |
| [[TUBB6]] | B | TUBB6 activity lowers PLXNA2's level | lines that do not express TUBB6 (11) vs lines expressing it (39) | 2.69× higher at baseline in the lines without TUBB6 | 0.068 | ⚠ within organs, on part of the lines; also absent: DNAAF9, CHST10, SYDE1 |
| [[PRSS16]] | B | PRSS16 activity lowers PLXNA2's level | lines that do not express PRSS16 (13) vs lines expressing it (37) | 1.68× higher at baseline in the lines without PRSS16 | 0.095 | ⚠ within organs, on part of the lines; also absent: STXBP2, MAP3K21, LINC00857 |
| [[TMEM144]] | C | TMEM144 activity lowers PLXNA2's level | lines that do not express TMEM144 (3) vs lines expressing it (47) | 4.41× higher at baseline in the lines without TMEM144 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: WNK4, RNF103-CHMP3, RBMS2; maybe low, not absent; its own permutation p |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 20, C 0. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ACOT7]] | B | PLXNA2 activity lowers ACOT7's level | lines that do not express PLXNA2 (15) vs lines expressing it (35) | 1.67× higher at baseline in the lines without PLXNA2 | 0.007 | ⚠ within organs, on part of the lines; also absent: GATA6, HS3ST3B1, IFI16 |
| [[HIPK2]] | B | PLXNA2 activity raises HIPK2's level | lines that do not express PLXNA2 (15) vs lines expressing it (35) | 2.17× lower at baseline in the lines without PLXNA2 | 0.009 | ⚠ within organs, on part of the lines; also absent: GATA6, HS3ST3B1, IFI16 |
| [[EMC2]] | B | PLXNA2 activity raises EMC2's level | lines that do not express PLXNA2 (15) vs lines expressing it (35) | 1.34× lower at baseline in the lines without PLXNA2 | 0.022 | ⚠ within organs, on part of the lines; also absent: GATA6, HS3ST3B1, IFI16 |
| [[FN1]] | B | PLXNA2 activity raises FN1's level | lines that do not express PLXNA2 (15) vs lines expressing it (35) | 3.71× lower at baseline in the lines without PLXNA2 | 0.025 | ⚠ within organs, on part of the lines; also absent: GATA6, HS3ST3B1, IFI16 |
| [[SH3PXD2A]] | B | PLXNA2 activity raises SH3PXD2A's level | lines that do not express PLXNA2 (15) vs lines expressing it (35) | 1.82× lower at baseline in the lines without PLXNA2 | 0.030 | ⚠ within organs, on part of the lines; also absent: GATA6, HS3ST3B1, IFI16 |
| [[LHFPL2]] | B | PLXNA2 activity raises LHFPL2's level | lines that do not express PLXNA2 (15) vs lines expressing it (35) | 2.14× lower at baseline in the lines without PLXNA2 | 0.033 | ⚠ within organs, on part of the lines; also absent: GATA6, HS3ST3B1, IFI16 |
| [[TESMIN]] | B | PLXNA2 activity lowers TESMIN's level | lines that do not express PLXNA2 (15) vs lines expressing it (35) | 1.87× higher at baseline in the lines without PLXNA2 | 0.033 | ⚠ within organs, on part of the lines; also absent: GATA6, HS3ST3B1, IFI16 |
| [[MAP4K4]] | B | PLXNA2 activity raises MAP4K4's level | lines that do not express PLXNA2 (15) vs lines expressing it (35) | 1.55× lower at baseline in the lines without PLXNA2 | 0.052 | ⚠ within organs, on part of the lines; also absent: GATA6, HS3ST3B1, IFI16 |
| [[HNRNPAB]] | B | PLXNA2 activity lowers HNRNPAB's level | lines that do not express PLXNA2 (15) vs lines expressing it (35) | 1.29× higher at baseline in the lines without PLXNA2 | 0.060 | ⚠ within organs, on part of the lines; also absent: GATA6, HS3ST3B1, IFI16 |
| [[YWHAB]] | B | PLXNA2 activity lowers YWHAB's level | lines that do not express PLXNA2 (15) vs lines expressing it (35) | 1.10× higher at baseline in the lines without PLXNA2 | 0.061 | ⚠ within organs, on part of the lines; also absent: GATA6, HS3ST3B1, IFI16 |
| cells under [[ERK5-IN-2 (drug)]] 5 µM | B | PLXNA2 activity raises the cells' numbers under ERK5-IN-2 5 µM (protects the cells) | lines that do not express PLXNA2 (15) vs lines expressing it (33) | the lines without PLXNA2: 0.81× the cells of the other lines | 0.074 | ⚠ within organs, on part of the lines; also absent: GATA6, HS3ST3B1, IFI16 |
| cells under [[Futibatinib (drug)]] 0.5 µM | B | PLXNA2 activity lowers the cells' numbers under Futibatinib 0.5 µM (makes them more sensitive) | lines that do not express PLXNA2 (15) vs lines expressing it (33) | the lines without PLXNA2: 1.15× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: GATA6, HS3ST3B1, IFI16 |

## Where it sits

- **Module**: [[Module 147]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.520). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (55.7, 8.6); signed map (11.4, 45.1). **Vector** length 94.2, 25.1% of its response variance represented; |z| ≥ 3 in 957 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.4 | +5.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +5.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.5 | +3.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.5 | +0.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.3 | +3.1 |
| fall | [[Selinexor (drug)]] 5 µM |  | -6.2 | -6.6 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -5.4 | -7.8 |
|  | [[Selinexor (drug)]] 0.05 µM |  | -3.1 | -4.8 |
|  | [[NG25 (drug)]] 5 µM |  | -2.7 | -4.1 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.5 | -3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | -1.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.1 | -5.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.1 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.0 | -2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.0 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | plexin A2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.2 — chr1:208,022,242-208,244,384 (-) |
| Ensembl biotype | protein_coding |
| Also known as | OCT, FLJ11751, FLJ30634, KIAA0463; previously PLXN2 |
| Gene groups (HGNC) | Plexins; IPT domain containing |
| Reactome | 7 pathways, smallest: SEMA3A-Plexin repulsion signaling by inhibiting Integrin adhesion; CRMPs in Sema3A signaling; Other semaphorin interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [O75051](https://www.uniprot.org/uniprotkb/O75051) (Plexin-A2):

> Coreceptor for SEMA3A and SEMA6A. Necessary for signaling by SEMA6A and class 3 semaphorins and subsequent remodeling of the cytoskeleton. Plays a role in axon guidance, invasive growth and cell migration. Class 3 semaphorins bind to a complex composed of a neuropilin and a plexin. The plexin modulates the affinity of the complex for specific semaphorins, and its cytoplasmic domain is required for the activation of down-stream signaling events in the cytoplasm (By similarity).

**Summary**, from NCBI Gene [5362](https://www.ncbi.nlm.nih.gov/gene/5362):

> This gene encodes a member of the plexin-A family of semaphorin co-receptors. Semaphorins are a large family of secreted or membrane-bound proteins that mediate repulsive effects on axon pathfinding during nervous system development. A subset of semaphorins are recognized by plexin-A/neuropilin transmembrane receptor complexes, triggering a cellular signal transduction cascade that leads to axon repulsion. This plexin-A family member is thought to transduce signals from semaphorin-3A and -3C. …

**Accessions** — [HGNC:9100](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9100) · Entrez [5362](https://www.ncbi.nlm.nih.gov/gene/5362) · UniProt [O75051](https://www.uniprot.org/uniprotkb/O75051) · Ensembl [ENSG00000076356](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000076356)

## Data

Gene col 1151: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1151); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1151, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1151]; `tensor/DDL_lfc|DDL_z.npy` [1151]; `embed/gene_vectors.npy` [1151]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1151 or target_col == 1151). Every well: [[PLXNA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLXNA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
