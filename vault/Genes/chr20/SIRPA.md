---
symbol: "SIRPA"
type: "gene"
col: 12520
ensembl_id: "ENSG00000198053"
name: "signal regulatory protein alpha"
location: "20p13"
module: 5
arm: "+"
pooled_cpm: 10.67
n_lines_expressing: 38
n_dd_up: 10
n_dd_down: 18
n_dd_up_clean: 5
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 2
direction_downstream: 7
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# SIRPA

*signal regulatory protein alpha* — 20p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.55× (z +9.2, q 2e-17, up in 18 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.259× (z -20.0, q 0e+00, down in 31 of 36 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TLCD3A]] (+0.61, fdr 2e-05), [[RHOBTB1]] (+0.57, fdr 5e-05), [[PRR5L]] (+0.56, fdr 2e-05); moves opposite to [[PKN2]] (-0.49, fdr 4e-05), [[IFTAP]] (-0.47, fdr 2e-04), [[CTNND1]] (-0.47, fdr 9e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SRPX]] → it (grade B ⚠); 7 go from it, the strongest it → [[CNPY4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12520.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +9.2 | 2e-17 | 18/32 (A549, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +4.7 | 7e-04 | 15/33 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +3.6 | 0.049 | 6/35 (HOP62, SW 900, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +3.6 | 0.049 | 9/35 (HS-578T, HOP62, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.27×** | +3.4 | 0.065 | 6/35 (SW480, HOP62, …) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.26×** | +3.4 | 0.065 | 5/35 (HOP62, RPMI-7951, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.25×** | +3.3 | 0.065 | 7/35 (HOP62, SW480, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.065 | 7/35 (RPMI-7951, HOP62, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.065 | 9/32 (RPMI-7951, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Larotrectinib (drug)]] 5 µM |  | 1.17× | +3.2 | 0.065 | 3/34 (SW 900, HOP62, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **1.52×** | +3.2 | 0.065 | 5/25 (SW480, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM |  | **1.26×** | +3.2 | 0.065 | 3/32 (C32, A498, …) | inconsistent across doses | position effect removed |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 1.24× | +3.0 | 0.10 | 1/32 (J82) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12520.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.259×** | -20.0 | 0e+00 | 31/36 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.327×** | -16.5 | 0e+00 | 31/36 (SW480, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.492×** | -14.8 | 0e+00 | 26/33 (C32, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.395×** | -13.7 | 8e-41 | 25/35 (NCI-H460, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.484×** | -10.7 | 8e-25 | 23/31 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.496×** | -10.0 | 2e-21 | 26/35 (RPMI-7951, C32, …) | rises with dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.574×** | -8.1 | 6e-14 | 20/36 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.641×** | -6.6 | 3e-09 | 19/36 (SK-MEL-2, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.669×** | -6.0 | 2e-07 | 14/31 (CFPAC-1, J82, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.537×** | -4.8 | 8e-05 | 14/31 (A-427, HS-578T, …) | rises with dose | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.741×** | -4.4 | 5e-04 | 14/35 (HS-578T, HOP62, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.816×** | -4.3 | 9e-04 | 14/35 (C32, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.585×** | -4.1 | 0.001 | 11/33 (SNU-1, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.592×** | -4.1 | 0.002 | 9/35 (NCI-H460, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.791×** | -3.3 | 0.033 | 9/32 (SK-MEL-2, SNU-423, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.804×** | -3.2 | 0.039 | 9/34 (NCI-H460, C32, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12520. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 21.2 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -23.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.142× (z -14.3) |
| [[C32 (line)]] | wt | 46.0 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0595× (z -30.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0838× (z -18.7) |
| [[RPMI-7951 (line)]] | alt | 34.7 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -13.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0856× (z -13.8) |
| [[A498 (line)]] | wt | 24.5 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -15.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.191× (z -12.7) |
| [[SK-MEL-2 (line)]] | alt | 47.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -14.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.219× (z -12.0) |
| [[A549 (line)]] | wt | 19.0 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +9.3) | [[Panobinostat (drug)]] 0.5 µM 0.173× (z -10.8) |
| [[SW480 (line)]] | alt | 12.0 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.135× (z -14.7) |
| [[HEC-1-A (line)]] | alt | 20.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -11.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.217× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 9.61 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0602× (z -13.0) |
| [[RKO (line)]] | wt | 11.3 | 0 | 3 (1 ⚠) | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0671× (z -11.7) |
| [[A-172 (line)]] | wt | 7.87 | 0 | 2 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0908× (z -11.0) |
| [[HS-578T (line)]] | alt | 21.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -15.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.178× (z -10.4) |
| [[SNU-1 (line)]] | wt | 33.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -10.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.151× (z -10.5) |
| [[CFPAC-1 (line)]] | alt | 10.3 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.170× (z -8.5) |
| [[J82 (line)]] | alt | 7.19 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.103× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[SW1417 (line)]] | alt | 5.50 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0841× (z -10.1) |
| [[A-427 (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.736 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.860 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 9.64 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.711 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.36 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.36 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.600 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.64 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.688 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.920 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12520), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TLCD3A]] | +0.61 | +0.46 / +0.50 | both halves | 2e-05 |  |
| [[RHOBTB1]] | +0.57 | +0.53 / +0.39 | both halves | 5e-05 |  |
| [[PRR5L]] | +0.56 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[DZIP1L]] | +0.55 | +0.59 / +0.37 | both halves | 8e-05 |  |
| [[TMEM11-DT]] | +0.54 | +0.39 / +0.49 | both halves | 5e-05 |  |
| [[PRDM15]] | +0.53 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[THAP4]] | +0.53 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[PTGFRN]] | +0.53 | +0.53 / +0.41 | both halves | 4e-05 | same gene group |
| [[TRABD2B]] | +0.52 | +0.38 / +0.55 | both halves | 7e-05 |  |
| [[ZNF142]] | +0.52 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[NDST1]] | +0.52 | +0.52 / +0.38 | both halves | 7e-05 |  |
| [[HCFC1]] | +0.52 | +0.41 / +0.46 | both halves | 4e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PKN2]] | -0.49 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[IFTAP]] | -0.47 | -0.30 / -0.47 | both halves | 2e-04 |  |
| [[CTNND1]] | -0.47 | -0.37 / -0.42 | both halves | 9e-05 | pathway: HALLMARK_APICAL_JUNCTION |
| [[DBP]] | -0.46 | -0.32 / -0.47 | both halves | 1e-04 |  |
| [[INIP]] | -0.46 | -0.38 / -0.32 | both halves | 2e-04 |  |
| [[PITPNA-AS1]] | -0.45 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[TMEM141]] | -0.45 | -0.31 / -0.30 | both halves | 2e-04 |  |
| [[MFSD4B]] | -0.45 | -0.38 / -0.48 | both halves | 7e-05 |  |
| [[RAD17]] | -0.44 | -0.34 / -0.29 | both halves | 2e-04 |  |
| [[TUFT1]] | -0.44 | -0.35 / -0.37 | both halves | 1e-04 |  |
| [[DDX19B]] | -0.43 | -0.24 / -0.38 | both halves | 4e-04 |  |
| [[TJP3]] | -0.43 | -0.33 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SRPX]] | B | SRPX activity raises SIRPA's level | lines that do not express SRPX (22) vs lines expressing it (28) | 2.19× lower at baseline in the lines without SRPX | 0.068 | ⚠ within organs, on part of the lines; also absent: COL15A1, ARHGEF6, ENSG00000230647 |
| [[TJP3]] | B | TJP3 activity lowers SIRPA's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 2.62× higher at baseline in the lines without TJP3 | 0.097 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1 |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CNPY4]] | B | SIRPA activity raises CNPY4's level | lines that do not express SIRPA (12) vs lines expressing it (38) | 1.92× lower at baseline in the lines without SIRPA | 0.007 | ⚠ within organs, on part of the lines; also absent: EID2B, LIX1L, FHL1 |
| [[TEAD2]] | B | SIRPA activity raises TEAD2's level | lines that do not express SIRPA (12) vs lines expressing it (38) | 2.34× lower at baseline in the lines without SIRPA | 0.012 | ⚠ within organs, on part of the lines; also absent: EID2B, LIX1L, FHL1 |
| [[SLC6A16]] | B | SIRPA activity raises SLC6A16's level | lines that do not express SIRPA (12) vs lines expressing it (38) | 2.62× lower at baseline in the lines without SIRPA | 0.019 | ⚠ within organs, on part of the lines; also absent: EID2B, LIX1L, FHL1 |
| [[PYGO1]] | B | SIRPA activity raises PYGO1's level | lines that do not express SIRPA (12) vs lines expressing it (38) | 4.76× lower at baseline in the lines without SIRPA | 0.023 | ⚠ within organs, on part of the lines; also absent: EID2B, LIX1L, FHL1 |
| [[TUFT1]] | B | SIRPA activity strengthens TUFT1's drug response | lines that do not express SIRPA (12) vs lines expressing it (33) | the lines without SIRPA respond 0.74× as strongly (z diff +1.98); strongest at Homoharringtonine 0.5 µM: 1.11x vs 2.33x (z diff +4.5) | 0.034 | ⚠ within organs, on part of the lines; also absent: EID2B, LIX1L, FHL1; target measured in part of the lines; artifact flags |
| [[GINS3]] | B | SIRPA activity raises GINS3's level | lines that do not express SIRPA (12) vs lines expressing it (38) | 1.53× lower at baseline in the lines without SIRPA | 0.037 | ⚠ within organs, on part of the lines; also absent: EID2B, LIX1L, FHL1 |
| [[SRPX]] | B | SIRPA activity raises SRPX's level | lines that do not express SIRPA (12) vs lines expressing it (38) | 3.73× lower at baseline in the lines without SIRPA | 0.064 | ⚠ within organs, on part of the lines; also absent: EID2B, LIX1L, FHL1 |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.378). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-14.2, 30.6); signed map (17.3, 23.1). **Vector** length 71.1, 13.8% of its response variance represented; |z| ≥ 3 in 879 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.2 | +9.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +3.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | +3.2 | +3.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.5 | +1.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.5 | +1.8 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.9 | -10.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.3 | -16.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.3 | -13.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.2 | -4.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.1 | -20.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.9 | -1.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.7 | -4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.2 | -3.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.1 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | signal regulatory protein alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p13 — chr20:1,894,167-1,940,592 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SHPS1, SIRP, MYD-1, BIT, P84, SHPS-1, SIRPalpha, CD172a; previously PTPNS1 |
| Gene groups (HGNC) | CD molecules; V-set domain containing; C1-set domain containing; Signal regulatory proteins; Ig-like cell adhesion molecule family |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 6 pathways, smallest: Signal regulatory protein family interactions; Cell surface interactions at the vascular wall; Cell-Cell communication |
| Matched by | ensembl_id |

**Function**, from UniProt [P78324](https://www.uniprot.org/uniprotkb/P78324) (Tyrosine-protein phosphatase non-receptor type substrate 1):

> Immunoglobulin-like cell surface receptor for CD47. Acts as docking protein and induces translocation of PTPN6, PTPN11 and other binding partners from the cytosol to the plasma membrane. Supports adhesion of cerebellar neurons, neurite outgrowth and glial cell attachment. May play a key role in intracellular signaling during synaptogenesis and in synaptic function (By similarity). Involved in the negative regulation of receptor tyrosine kinase-coupled cellular responses induced by cell …

**Summary**, from NCBI Gene [140885](https://www.ncbi.nlm.nih.gov/gene/140885):

> The protein encoded by this gene is a member of the signal-regulatory-protein (SIRP) family, and also belongs to the immunoglobulin superfamily. SIRP family members are receptor-type transmembrane glycoproteins known to be involved in the negative regulation of receptor tyrosine kinase-coupled signaling processes. This protein can be phosphorylated by tyrosine kinases. The phospho-tyrosine residues of this PTP have been shown to recruit SH2 domain containing tyrosine phosphatases (PTP), and …

**Accessions** — [HGNC:9662](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9662) · Entrez [140885](https://www.ncbi.nlm.nih.gov/gene/140885) · UniProt [P78324](https://www.uniprot.org/uniprotkb/P78324) · Ensembl [ENSG00000198053](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198053)

## Data

Gene col 12520: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12520); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12520, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12520]; `tensor/DDL_lfc|DDL_z.npy` [12520]; `embed/gene_vectors.npy` [12520]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12520 or target_col == 12520). Every well: [[SIRPA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SIRPA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
