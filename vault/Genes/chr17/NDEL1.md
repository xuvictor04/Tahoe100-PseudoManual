---
symbol: "NDEL1"
type: "gene"
col: 9334
ensembl_id: "ENSG00000166579"
name: "nudE neurodevelopment protein 1 like 1"
location: "17p13.1"
module: 56
arm: "+"
pooled_cpm: 135.43
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 24
n_dd_up_clean: 0
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# NDEL1

*nudE neurodevelopment protein 1 like 1* — 17p13.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 2.16×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (C32 2.27×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.463× (z -11.2, q 4e-26, down in 46 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.577× (z -7.7, q 2e-12, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDXDC1]] (+0.82, fdr 7e-06), [[PDXDC2P]] (+0.80, fdr 7e-06), [[TXNDC11]] (+0.80, fdr 7e-06); moves opposite to [[NHLRC2]] (-0.63, fdr 1e-05), [[SLC25A13]] (-0.60, fdr 1e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9334.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 2.16×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (C32 2.27×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | 1.55× | +3.3 | 0.40 | 30/49 (HEC-1-A, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | 1.53× | +3.2 | 0.40 | 23/48 (MIA PaCa-2, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9334.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.463×** | -11.2 | 4e-26 | 46/49 (A-427, A498, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.525×** | -9.0 | 7e-17 | 38/44 (SNU-1, A498, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.525×** | -8.6 | 1e-15 | 43/45 (HS-578T, A498, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.577×** | -7.7 | 2e-12 | 37/48 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.627×** | -6.8 | 1e-09 | 38/48 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.745×** | -5.8 | 5e-07 | 33/48 (RPMI-7951, A498, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.701×** | -5.0 | 5e-05 | 36/48 (HS-578T, A549, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.714×** | -4.9 | 7e-05 | 34/48 (LoVo, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.744×** | -4.3 | 0.001 | 31/48 (LoVo, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.808×** | -4.2 | 0.001 | 28/48 (NCI-H1573, HS-578T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.743×** | -4.1 | 0.002 | 30/47 (hTERT-HPNE, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.757×** | -4.1 | 0.002 | 28/48 (A-172, HS-578T, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.825×** | -3.7 | 0.008 | 28/48 (CFPAC-1, LoVo, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.777×** | -3.7 | 0.010 | 25/48 (A-172, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.790×** | -3.4 | 0.023 | 25/48 (NCI-H2347, A-172, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.645×** | -3.3 | 0.031 | 24/49 (HS-578T, A498, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.803×** | -3.2 | 0.045 | 25/48 (SNU-423, hTERT-HPNE, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.814×** | -3.0 | 0.078 | 23/49 (J82, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.676×** | -3.0 | 0.078 | 22/49 (AsPC-1, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.817×** | -3.0 | 0.082 | 20/48 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.820×** | -2.9 | 0.094 | 20/49 (HCT15, COLO 205, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.821×** | -2.9 | 0.094 | 24/48 (hTERT-HPNE, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9334. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 155 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -15.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.275× (z -15.2) |
| [[HS-578T (line)]] | alt | 216 | 0 | 8 (5 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.286× (z -14.0) |
| [[A498 (line)]] | wt | 258 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.250× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.301× (z -14.4) |
| [[A549 (line)]] | wt | 215 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.269× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.369× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 104 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.337× (z -14.2) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.375× (z -12.3) |
| [[HOP62 (line)]] | alt | 153 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.341× (z -10.7) |
| [[hTERT-HPNE (line)]] | wt | 191 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.317× (z -10.0) |
| [[Hs 766T (line)]] | wt | 151 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.294× (z -11.4) |
| [[J82 (line)]] | alt | 129 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.413× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.435× (z -9.2) |
| [[LoVo (line)]] | wt | 237 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.385× (z -9.8) |
| [[KATO III (line)]] | alt | 166 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[RPMI-7951 (line)]] | alt | 146 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.316× (z -11.2) |
| [[SNU-1 (line)]] | wt | 131 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.110× (z -19.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SW 900 (line)]] | alt | 215 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.189× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A-427 (line)]] | wt | 86.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -19.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[AN3 CA (line)]] | alt | 89.0 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.239× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 229 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.304× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[C32 (line)]] | wt | 93.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HCT15 (line)]] | alt | 151 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[MIA PaCa-2 (line)]] | alt | 121 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +10.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H1792 (line)]] | alt | 76.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.305× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 141 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.285× (z -10.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 134 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.318× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SNU-423 (line)]] | alt | 104 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.379× (z -9.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.428× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[BT-474 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 81.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 90.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 138 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 115 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 88.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 87.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 80.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 172 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 120 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 97.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 94.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 64.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 122 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 89.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 226 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 140 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 143 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9334), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDXDC1]] | +0.82 | +0.82 / +0.82 | both halves | 7e-06 |  |
| [[PDXDC2P]] | +0.80 | +0.80 / +0.81 | both halves | 7e-06 |  |
| [[TXNDC11]] | +0.80 | +0.79 / +0.78 | both halves | 7e-06 |  |
| [[SEC31A]] | +0.79 | +0.79 / +0.79 | both halves | 7e-06 |  |
| [[COPA]] | +0.78 | +0.79 / +0.74 | both halves | 7e-06 |  |
| [[DHDDS]] | +0.77 | +0.81 / +0.73 | both halves | 7e-06 |  |
| [[SEC24D]] | +0.75 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[KDELR2]] | +0.75 | +0.78 / +0.74 | both halves | 7e-06 |  |
| [[EIF2AK3]] | +0.73 | +0.74 / +0.72 | both halves | 7e-06 |  |
| [[COPB1]] | +0.73 | +0.79 / +0.64 | both halves | 7e-06 |  |
| [[DDB1]] | +0.73 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[GOLT1B]] | +0.73 | +0.72 / +0.76 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NHLRC2]] | -0.63 | -0.65 / -0.57 | both halves | 1e-05 |  |
| [[SLC25A13]] | -0.60 | -0.63 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.817). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.0, -32.9); signed map (-50.1, 9.9). **Vector** length 127, 47.1% of its response variance represented; |z| ≥ 3 in 1,052 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Asparagine N-linked glycosylation* (reactome, mean cos +0.65 to 23); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.66 to 16); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.66 to 16).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.5 | +1.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | -1.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | -2.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | +4.1 | -3.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | -1.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.3 | +1.0 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +2.3 | +1.7 |
|  | [[Cloxacillin (sodium) (drug)]] 0.05 µM |  | +2.1 | +2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.0 | +1.5 |
|  | [[Fluvoxamine (maleate) (drug)]] 5 µM |  | +2.0 | +1.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.5 | -7.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.4 | -6.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.4 | -2.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | -5.7 | -3.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.6 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.1 | -4.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.3 | -2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.1 | -5.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.0 | -3.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | nudE neurodevelopment protein 1 like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:8,413,131-8,490,411 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NUDEL, MITAP1, NDE1L1, NDE2 |
| Reactome | 17 pathways, smallest: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; Amplification of signal from the kinetochores; EML4 and NUDC in mitotic spindle formation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9GZM8](https://www.uniprot.org/uniprotkb/Q9GZM8) (Nuclear distribution protein nudE-like 1):

> Required for organization of the cellular microtubule array and microtubule anchoring at the centrosome. May regulate microtubule organization at least in part by targeting the microtubule severing protein KATNA1 to the centrosome. Also positively regulates the activity of the minus-end directed microtubule motor protein dynein. May enhance dynein-mediated microtubule sliding by targeting dynein to the microtubule plus ends. Required for several dynein- and microtubule-dependent processes such …

**Summary**, from NCBI Gene [81565](https://www.ncbi.nlm.nih.gov/gene/81565):

> Enables identical protein binding activity. Involved in chromosome segregation; positive regulation of GTPase activity; and regulation of intracellular protein transport. Located in kinetochore. Biomarker of schizophrenia. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17620](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17620) · Entrez [81565](https://www.ncbi.nlm.nih.gov/gene/81565) · UniProt [Q9GZM8](https://www.uniprot.org/uniprotkb/Q9GZM8) · Ensembl [ENSG00000166579](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166579)

## Data

Gene col 9334: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9334); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9334, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9334]; `tensor/DDL_lfc|DDL_z.npy` [9334]; `embed/gene_vectors.npy` [9334]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9334 or target_col == 9334). Every well: [[NDEL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDEL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
