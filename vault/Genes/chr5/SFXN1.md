---
symbol: "SFXN1"
type: "gene"
col: 8952
ensembl_id: "ENSG00000164466"
name: "sideroflexin 1"
location: "5q35.2"
module: 105
arm: "+"
pooled_cpm: 141.73
n_lines_expressing: 49
n_dd_up: 0
n_dd_down: 21
n_dd_up_clean: 0
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/105"]
generated_by: "tahoemap"
---

# SFXN1

*sideroflexin 1* — 5q35.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (J82 1.99×, SW480 1.84×; ⚠ cell-cycle shift, explains ~40% of this change).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.314× (z -30.9, q 0e+00, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDK3]] (+0.74, fdr 7e-06), [[YEATS2]] (+0.70, fdr 7e-06), [[SNAPC3]] (+0.67, fdr 7e-06); moves opposite to [[PPP3CB-AS1]] (-0.65, fdr 7e-06), [[DDX5]] (-0.56, fdr 3e-05), [[ANKLE2]] (-0.55, fdr 3e-05).
> It is in [[Module 105]], a single-armed module (Late Phase of HIV Life Cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8952.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (J82 1.99×, SW480 1.84×; ⚠ cell-cycle shift, explains ~40% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Abemaciclib (drug)]] 5 µM |  | 1.42× | +3.5 | 0.10 | 18/47 (SK-MEL-2, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | 1.20× | +3.4 | 0.10 | 21/47 (SW480, J82, …) | inconsistent across doses | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 1.41× | +3.4 | 0.10 | 18/37 (NCI-H1573, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 1.41× | +3.4 | 0.10 | 24/46 (RPMI-7951, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.12× | +3.2 | 0.15 | 10/47 (LoVo, SNU-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 1.18× | +3.2 | 0.15 | 23/47 (J82, SW480, …) | rises with dose | composition shift |
| [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | 1.12× | +3.1 | 0.15 | 3/48 (Panc 03.27, HOP62, …) | rises with dose |  |
| [[Terfenadine (drug)]] 5 µM |  | 1.12× | +3.1 | 0.15 | 8/47 (RPMI-7951, H4, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | 1.36× | +3.0 | 0.15 | 22/48 (HEC-1-A, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8952.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.314×** | -30.9 | 0e+00 | 46/47 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.524×** | -17.2 | 0e+00 | 45/48 (H4, HS-578T, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.413×** | -16.0 | 0e+00 | 46/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.441×** | -15.4 | 0e+00 | 46/47 (A-427, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.524×** | -12.2 | 5e-32 | 45/47 (MIA PaCa-2, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.556×** | -11.1 | 2e-26 | 46/47 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.858× | -10.1 | 4e-22 | 9/49 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.669×** | -7.6 | 3e-12 | 42/47 (MIA PaCa-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.688×** | -6.8 | 9e-10 | 33/47 (HS-578T, SW 900, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.792×** | -6.2 | 4e-08 | 29/47 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.726×** | -5.8 | 4e-07 | 38/47 (MIA PaCa-2, RKO, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.785×** | -4.5 | 3e-04 | 28/47 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.774×** | -4.4 | 4e-04 | 25/44 (C-33 A, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.803×** | -4.1 | 0.002 | 25/47 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.806×** | -4.0 | 0.002 | 28/48 (hTERT-HPNE, PANC-1, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.800×** | -4.0 | 0.002 | 27/49 (SW 1088, SW480, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.821×** | -3.7 | 0.007 | 24/47 (HEC-1-A, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8952. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 235 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -22.9) |
| [[MIA PaCa-2 (line)]] | alt | 178 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -25.1) |
| [[SW 900 (line)]] | alt | 282 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -19.9) |
| [[SW48 (line)]] | wt | 218 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -15.2) |
| [[SW480 (line)]] | alt | 143 | 1 (1 ⚠) | 6 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.84× (z +9.1) ⚠ cell-cycle shift, explains ~40% of this change | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -16.8) |
| [[A498 (line)]] | wt | 107 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -28.7) |
| [[NCI-H23 (line)]] | alt | 112 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -18.9) |
| [[NCI-H2347 (line)]] | alt | 183 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -26.9) |
| [[RPMI-7951 (line)]] | alt | 147 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -23.4) |
| [[H4 (line)]] | wt | 286 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -17.5) |
| [[HCT15 (line)]] | alt | 283 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -17.6) |
| [[HOP62 (line)]] | alt | 210 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -18.9) |
| [[Hs 766T (line)]] | wt | 134 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -15.2) |
| [[HS-578T (line)]] | alt | 156 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -23.5) |
| [[NCI-H460 (line)]] | wt | 164 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -30.2) |
| [[SK-MEL-2 (line)]] | alt | 80.8 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -19.0) |
| [[A-172 (line)]] | wt | 133 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -18.6) |
| [[AsPC-1 (line)]] | alt | 125 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -25.2) |
| [[C32 (line)]] | wt | 45.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -21.9) |
| [[J82 (line)]] | alt | 134 | 1 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.99× (z +9.2) ⚠ cell-cycle shift, explains ~40% of this change | [[Homoharringtonine (drug)]] 5 µM 0.534× (z -11.7) |
| [[NCI-H2030 (line)]] | alt | 124 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -28.5) |
| [[PANC-1 (line)]] | alt | 102 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -25.6) |
| [[RKO (line)]] | wt | 131 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -23.7) |
| [[A-427 (line)]] | wt | 145 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.210× (z -22.1) |
| [[C-33 A (line)]] | alt | 161 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.209× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 154 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -23.9) |
| [[COLO 205 (line)]] | alt | 116 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -17.7) |
| [[hTERT-HPNE (line)]] | wt | 138 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -22.1) |
| [[LoVo (line)]] | wt | 134 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -23.0) |
| [[LS 180 (line)]] | wt | 162 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -19.7) |
| [[NCI-H1573 (line)]] | alt | 124 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -21.0) |
| [[NCI-H1792 (line)]] | alt | 112 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -22.9) |
| [[SNU-1 (line)]] | wt | 170 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -12.9) |
| [[SNU-423 (line)]] | alt | 134 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -25.8) |
| [[SW1417 (line)]] | alt | 132 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -19.0) |
| [[BT-474 (line)]] | alt | 96.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -12.5) |
| [[HepG2_C3A (line)]] | wt | 137 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -12.3) |
| [[KATO III (line)]] | alt | 113 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -21.4) |
| [[Panc 03.27 (line)]] | alt | 119 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -13.7) |
| [[A549 (line)]] | wt | 140 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -11.7) |
| [[HT-29 (line)]] | alt | 107 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -13.7) |
| [[SW 1088 (line)]] | alt | 259 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -9.9) |
| [[SW 1271 (line)]] | alt | 194 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -11.3) |
| [[AN3 CA (line)]] | alt | 157 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 134 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 69.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 132 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8952), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDK3]] | +0.74 | +0.81 / +0.64 | both halves | 7e-06 |  |
| [[YEATS2]] | +0.70 | +0.78 / +0.60 | both halves | 7e-06 |  |
| [[SNAPC3]] | +0.67 | +0.75 / +0.58 | both halves | 7e-06 |  |
| [[INSIG2]] | +0.67 | +0.74 / +0.58 | both halves | 7e-06 |  |
| [[POM121C]] | +0.66 | +0.77 / +0.61 | both halves | 7e-06 |  |
| [[POM121]] | +0.66 | +0.79 / +0.61 | both halves | 7e-06 |  |
| [[SPICE1]] | +0.65 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[HERC3]] | +0.65 | +0.74 / +0.56 | both halves | 1e-05 |  |
| [[GMCL1]] | +0.65 | +0.76 / +0.57 | both halves | 1e-05 |  |
| [[HACE1]] | +0.65 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[FAM210A]] | +0.64 | +0.74 / +0.55 | both halves | 1e-05 |  |
| [[PRKRIP1]] | +0.63 | +0.72 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP3CB-AS1]] | -0.65 | -0.72 / -0.69 | both halves | 7e-06 |  |
| [[DDX5]] | -0.56 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[ANKLE2]] | -0.55 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[DNAJB12]] | -0.55 | -0.57 / -0.46 | both halves | 2e-05 |  |
| [[ZNF747]] | -0.55 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[ZNF407-AS1]] | -0.54 | -0.65 / -0.36 | both halves | 9e-05 |  |
| [[CFLAR]] | -0.54 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[INO80D]] | -0.54 | -0.56 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SFXN1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ZNF215]] | B | ZNF215 activity raises SFXN1's level | lines that do not express ZNF215 (12) vs lines expressing it (38) | 1.08× lower at baseline in the lines without ZNF215 | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000283415, ENSG00000291143 |
| [[RAB20]] | B | RAB20 activity raises SFXN1's level | lines that do not express RAB20 (8) vs lines expressing it (42) | 1.52× lower at baseline in the lines without RAB20 | 0.0997 | ⚠ within organs, on part of the lines; also absent: RPS6KA2, PRDX2, YPEL3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 105]] — Late Phase of HIV Life Cycle; 44 genes; every member is in the + arm (projection on the module's main direction 0.738). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.7, -19.1); signed map (-39.1, 22.3). **Vector** length 124, 43.0% of its response variance represented; |z| ≥ 3 in 1,067 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.0 | +3.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +7.6 | +2.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.6 | -4.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.6 | -7.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.2 | +0.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.1 | -1.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.5 | +2.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.3 | +2.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.1 | +3.5 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -9.0 | -16.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.0 | -15.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.6 | -30.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.1 | -4.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | -4.9 | -3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.9 | -5.8 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -4.3 | -4.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.1 | -2.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -4.0 | -2.5 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.3 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | sideroflexin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.2 — chr5:175,477,062-175,529,742 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12876, SLC56A1 |
| Gene groups (HGNC) | Solute carrier family 56, sideroflexins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H9B4](https://www.uniprot.org/uniprotkb/Q9H9B4) (Sideroflexin-1):

> Amino acid transporter importing serine, an essential substrate of the mitochondrial branch of the one-carbon pathway, into mitochondria. Mitochondrial serine is then converted to glycine and formate, which exits to the cytosol where it is used to generate the charged folates that serve as one-carbon donors. May also transport other amino acids including alanine and cysteine.

**Summary**, from NCBI Gene [94081](https://www.ncbi.nlm.nih.gov/gene/94081):

> Enables L-alanine transmembrane transporter activity and L-serine transmembrane transporter activity. Involved in L-alanine transport; L-serine transport; and serine import into mitochondrion. Located in mitochondrial inner membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16085](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16085) · Entrez [94081](https://www.ncbi.nlm.nih.gov/gene/94081) · UniProt [Q9H9B4](https://www.uniprot.org/uniprotkb/Q9H9B4) · Ensembl [ENSG00000164466](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164466)

## Data

Gene col 8952: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8952); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8952, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8952]; `tensor/DDL_lfc|DDL_z.npy` [8952]; `embed/gene_vectors.npy` [8952]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8952 or target_col == 8952). Every well: [[SFXN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SFXN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
