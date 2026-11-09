---
symbol: "BIN1"
type: "gene"
col: 5893
ensembl_id: "ENSG00000136717"
name: "bridging integrator 1"
location: "2q14.3"
module: 98
arm: "+"
pooled_cpm: 18.97
n_lines_expressing: 46
n_dd_up: 19
n_dd_down: 5
n_dd_up_clean: 10
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/098"]
generated_by: "tahoemap"
---

# BIN1

*bridging integrator 1* — 2q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.01× (z +15.9, q 0e+00, up in 34 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.33× (z +5.8, q 6e-07, up in 18 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.713× (z -6.9, q 3e-09, down in 27 of 44 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.540× (z -4.6, q 1e-03, down in 15 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NFIC]] (+0.57, fdr 2e-05), [[DIP2C]] (+0.56, fdr 1e-05), [[INF2]] (+0.53, fdr 6e-05); moves opposite to [[AADACP1]] (-0.47, fdr 3e-05), [[CRLF2]] (-0.44, fdr 4e-05), [[GJA1]] (-0.43, fdr 1e-04).
> It is in [[Module 098]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FST]] → it (grade B ⚠); 1 goes from it, the strongest it → [[GAS6]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5893.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.01×** | +15.9 | 0e+00 | 34/35 (A498, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.41×** | +12.2 | 1e-31 | 20/25 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.91×** | +7.8 | 2e-12 | 26/30 (KATO III, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +6.0 | 4e-07 | 27/39 (NCI-H1792, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +5.8 | 6e-07 | 18/41 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.49×** | +5.8 | 7e-07 | 22/40 (SW480, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~24% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.42×** | +5.0 | 4e-05 | 18/41 (HOP62, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +5.0 | 5e-05 | 21/43 (HEC-1-A, LoVo, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +4.5 | 4e-04 | 22/43 (HEC-1-A, J82, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.35×** | +4.3 | 0.001 | 15/43 (J82, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.22×** | +4.1 | 0.002 | 15/43 (NCI-H23, PANC-1, …) | top dose only | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.32×** | +3.9 | 0.005 | 16/44 (NCI-H1573, PANC-1, …) | top dose only | composition shift; position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **1.21×** | +3.8 | 0.005 | 12/44 (PANC-1, RKO, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.30×** | +3.6 | 0.013 | 14/43 (RPMI-7951, HEC-1-A, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.022 | 8/44 (A-172, HOP62, …) | rises with dose |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.25×** | +3.2 | 0.046 | 9/42 (HOP62, NCI-H2347, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.25×** | +3.1 | 0.072 | 11/42 (Hs 766T, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Budesonide (drug)]] 0.05 µM |  | **1.23×** | +2.9 | 0.099 | 12/42 (HOP62, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5893.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.713×** | -6.9 | 3e-09 | 27/44 (HT-29, NCI-H1573, …) | all doses, stronger at high dose | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **0.540×** | -4.6 | 1e-03 | 15/44 (SW480, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.732×** | -4.5 | 0.001 | 19/44 (SNU-1, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.575×** | -4.2 | 0.004 | 15/40 (HS-578T, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.791×** | -3.4 | 0.087 | 12/43 (CHP-212, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.810× | -3.0 | 0.24 | 6/44 (HEC-1-A, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5893. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 15.8 | 8 (1 ⚠) | 0 | [[Budesonide (drug)]] 0.5 µM 4.87× (z +9.7) | — |
| [[A498 (line)]] | wt | 48.7 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.98× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[Triamcinolone (drug)]] 5 µM 1.92× (z +8.6) | — |
| [[NCI-H460 (line)]] | wt | 16.8 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.71× (z +9.6) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +8.9) | — |
| [[A-172 (line)]] | wt | 23.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +10.5) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[PANC-1 (line)]] | alt | 20.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +10.5) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[A549 (line)]] | wt | 8.40 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.63× (z +9.9) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[AN3 CA (line)]] | alt | 25.8 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0739× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 25.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.433× (z -9.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[LS 180 (line)]] | wt | 18.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.65× (z +8.7) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 25.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.20× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 12.0 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 5.99× (z +9.0) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[NCI-H1792 (line)]] | alt | 18.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.66× (z +11.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 36.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +10.3) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 16.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.65× (z +12.4) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[SNU-1 (line)]] | wt | 18.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.124× (z -9.2) |
| [[SNU-423 (line)]] | alt | 13.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.13× (z +8.8) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 8.88 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.36 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.34 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 20.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5893), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFIC]] | +0.57 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[DIP2C]] | +0.56 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[INF2]] | +0.53 | +0.38 / +0.51 | both halves | 6e-05 |  |
| [[TRAF7]] | +0.52 | +0.33 / +0.60 | both halves | 1e-04 |  |
| [[KLF9]] | +0.51 | +0.57 / +0.46 | both halves | 2e-05 |  |
| [[CRTC2]] | +0.50 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[MAOA]] | +0.50 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[ACSL1]] | +0.50 | +0.43 / +0.53 | both halves | 3e-05 | pathway: HALLMARK_MYOGENESIS |
| [[NCOR2]] | +0.50 | +0.26 / +0.58 | both halves | 4e-04 |  |
| [[RIPOR1]] | +0.49 | +0.49 / +0.41 | both halves | 4e-05 |  |
| [[FAH]] | +0.49 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[NEBL]] | +0.49 | +0.43 / +0.49 | both halves | 4e-05 | same gene group |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AADACP1]] | -0.47 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[CRLF2]] | -0.44 | -0.48 / -0.40 | both halves | 4e-05 |  |
| [[GJA1]] | -0.43 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[C12orf75-AS1]] | -0.43 | -0.46 / -0.38 | both halves | 7e-05 |  |
| [[BMPER]] | -0.42 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[TMEM158]] | -0.42 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[FST]] | -0.41 | -0.36 / -0.40 | both halves | 1e-04 | pathway: HALLMARK_MYOGENESIS |
| [[VEGFC]] | -0.40 | -0.41 / -0.38 | both halves | 6e-05 |  |
| [[IMP3]] | -0.39 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[POLR2K]] | -0.39 | -0.34 / -0.24 | both halves | 5e-04 |  |
| [[IL1B]] | -0.39 | -0.39 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FST]] | B | FST activity strengthens BIN1's drug response | lines that do not express FST (24) vs lines expressing it (20) | the lines without FST respond 0.81× as strongly (z diff +0.61); strongest at Idarubicin (hydrochloride) 5 µM: 1.06x vs 1.62x (z diff +3.0) | 0.096 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IDO1, FN1, CDH2; target measured in part of the lines; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GAS6]] | C | BIN1 activity raises GAS6's level | lines that do not express BIN1 (4) vs lines expressing it (46) | 3.81× lower at baseline in the lines without BIN1 | 0.042 | ⚠ few lines (4 vs 46); across organs; also absent: PORCN |

## Where it sits

- **Module**: [[Module 098]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.526). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.9, 13.4); signed map (15.4, 32.9). **Vector** length 77.4, 15.4% of its response variance represented; |z| ≥ 3 in 800 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +15.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +12.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | +4.2 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +7.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.7 | +6.0 |
|  | [[Budesonide (drug)]] 5 µM |  | +3.0 | +1.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.5 | +1.1 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.5 | +3.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.4 | +1.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.4 | +2.1 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -4.8 | -6.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -3.2 | -3.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.5 | -4.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -1.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.3 | -1.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.2 | -1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.2 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | bridging integrator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.3 — chr2:127,048,027-127,107,288 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SH3P9, AMPH2; previously AMPHL |
| Gene groups (HGNC) | N-BAR domain containing; SH3 domain containing |
| Hallmark sets | MYOGENESIS, MITOTIC_SPINDLE |
| Reactome | 3 pathways, smallest: Clathrin-mediated endocytosis; Membrane Trafficking; Vesicle-mediated transport |
| Matched by | ensembl_id |

**Function**, from UniProt [O00499](https://www.uniprot.org/uniprotkb/O00499) (Myc box-dependent-interacting protein 1):

> Is a key player in the control of plasma membrane curvature, membrane shaping and membrane remodeling. Required in muscle cells for the formation of T-tubules, tubular invaginations of the plasma membrane that function in depolarization-contraction coupling. Is a negative regulator of endocytosis (By similarity). Is also involved in the regulation of intracellular vesicles sorting, modulation of BACE1 trafficking and the control of amyloid-beta production. In neuronal circuits, endocytosis …

**Summary**, from NCBI Gene [274](https://www.ncbi.nlm.nih.gov/gene/274):

> This gene encodes several isoforms of a nucleocytoplasmic adaptor protein, one of which was initially identified as a MYC-interacting protein with features of a tumor suppressor. Isoforms that are expressed in the central nervous system may be involved in synaptic vesicle endocytosis and may interact with dynamin, synaptojanin, endophilin, and clathrin. Isoforms that are expressed in muscle and ubiquitously expressed isoforms localize to the cytoplasm and nucleus and activate a …

**Accessions** — [HGNC:1052](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1052) · Entrez [274](https://www.ncbi.nlm.nih.gov/gene/274) · UniProt [O00499](https://www.uniprot.org/uniprotkb/O00499) · Ensembl [ENSG00000136717](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136717)

## Data

Gene col 5893: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5893); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5893, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5893]; `tensor/DDL_lfc|DDL_z.npy` [5893]; `embed/gene_vectors.npy` [5893]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5893 or target_col == 5893). Every well: [[BIN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BIN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
