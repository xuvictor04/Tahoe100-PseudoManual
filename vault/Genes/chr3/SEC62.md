---
symbol: "SEC62"
type: "gene"
col: 183
ensembl_id: "ENSG00000008952"
name: "SEC62 preprotein translocation factor"
location: "3q26.2"
module: 12
arm: "+"
pooled_cpm: 188.28
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 2
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# SEC62

*SEC62 preprotein translocation factor* — 3q26.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.94× (z +9.6, q 5e-19, up in 48 of 48 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.67× (z +6.6, q 7e-09, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.791× (z -4.8, q 0.001, down in 29 of 49 measured lines) ⚠ cell-cycle shift, explains ~23% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (RKO 0.524×, Panc 03.27 0.575×, LoVo 0.572×, HT-29 0.602×; ⚠ cell-cycle shift, explains ~23% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (H4 0.399×; ⚠ cell-cycle shift, explains ~25% of this change); [[Atazanavir (sulfate) (drug)]] 5 µM in 1 line (NCI-H596 0.312×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPIG]] (+0.78, fdr 7e-06), [[AKAP9]] (+0.77, fdr 7e-06), [[PIGBOS1]] (+0.76, fdr 7e-06); moves opposite to [[AKT1]] (-0.75, fdr 7e-06), [[SLC25A39]] (-0.69, fdr 7e-06), [[COLGALT1]] (-0.69, fdr 7e-06).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 10 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 183.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.94×** | +9.6 | 5e-19 | 48/48 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.52×** | +8.5 | 5e-15 | 41/48 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.79×** | +8.1 | 1e-13 | 46/48 (NCI-H1573, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.67×** | +6.6 | 7e-09 | 47/48 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.53×** | +6.2 | 7e-08 | 45/48 (A-427, C32, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.51×** | +6.0 | 2e-07 | 43/48 (NCI-H1573, LS 180, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.46×** | +5.4 | 4e-06 | 37/48 (NCI-H1573, LS 180, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~61% of this change | **1.37×** | +4.6 | 3e-04 | 36/48 (NCI-H2030, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.42×** | +4.5 | 4e-04 | 31/49 (A549, NCI-H23, …) | two highest doses | composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.40×** | +4.5 | 5e-04 | 37/47 (A-427, C32, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.30×** | +3.8 | 0.007 | 29/48 (NCI-H1573, H4, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | **1.30×** | +3.7 | 0.010 | 28/44 (NCI-H1573, SHP-77, …) | two highest doses | composition shift |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.52×** | +3.2 | 0.063 | 30/49 (NCI-H1573, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 183.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (RKO 0.524×, Panc 03.27 0.575×, LoVo 0.572×, HT-29 0.602×; ⚠ cell-cycle shift, explains ~23% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (H4 0.399×; ⚠ cell-cycle shift, explains ~25% of this change); [[Atazanavir (sulfate) (drug)]] 5 µM in 1 line (NCI-H596 0.312×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.791×** | -4.8 | 0.001 | 29/49 (RKO, Panc 03.27, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.910× | -4.2 | 0.007 | 3/50 (NCI-H23, SW 1271, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.771×** | -3.6 | 0.064 | 29/48 (H4, AN3 CA, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 0.792× | -3.3 | 0.12 | 24/48 (SW1417, Hs 766T, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 183. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 159 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +15.0) ⚠ cell-cycle shift, explains ~74% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.50× (z +9.5) | — |
| [[HEC-1-A (line)]] | alt | 242 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +14.2) ⚠ cell-cycle shift, explains ~74% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 1.96× (z +8.6) | — |
| [[LS 180 (line)]] | wt | 153 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +12.5) ⚠ cell-cycle shift, explains ~74% of this change | — |
| [[PANC-1 (line)]] | alt | 147 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +12.3) ⚠ cell-cycle shift, explains ~74% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 2.12× (z +8.6) | — |
| [[A-427 (line)]] | wt | 293 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.05 µM 2.42× (z +10.2) | — |
| [[SW480 (line)]] | alt | 182 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +9.9) ⚠ cell-cycle shift, explains ~74% of this change | — |
| [[A-172 (line)]] | wt | 226 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +9.2) ⚠ cell-cycle shift, explains ~74% of this change | — |
| [[H4 (line)]] | wt | 216 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.45× (z +9.5) ⚠ cell-cycle shift, explains ~25% of this change | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -9.3) ⚠ cell-cycle shift, explains ~25% of this change |
| [[HT-29 (line)]] | alt | 236 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +9.1) ⚠ cell-cycle shift, explains ~74% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.602× (z -9.0) ⚠ cell-cycle shift, explains ~23% of this change |
| [[LoVo (line)]] | wt | 165 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.09× (z +8.7) ⚠ cell-cycle shift, explains ~25% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -9.3) ⚠ cell-cycle shift, explains ~23% of this change |
| [[LOX-IMVI (line)]] | wt | 195 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +10.0) ⚠ cell-cycle shift, explains ~74% of this change | — |
| [[A549 (line)]] | wt | 194 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +10.9) ⚠ cell-cycle shift, explains ~74% of this change | — |
| [[BT-474 (line)]] | alt | 168 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +10.1) ⚠ cell-cycle shift, explains ~74% of this change | — |
| [[C32 (line)]] | wt | 130 | 1 | 0 | [[Homoharringtonine (drug)]] 0.05 µM 2.38× (z +9.0) | — |
| [[COLO 205 (line)]] | alt | 186 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +11.2) ⚠ cell-cycle shift, explains ~74% of this change | — |
| [[KATO III (line)]] | alt | 246 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +9.5) ⚠ cell-cycle shift, explains ~74% of this change | — |
| [[NCI-H596 (line)]] | alt | 180 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 5 µM 0.312× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 248 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.575× (z -9.4) ⚠ cell-cycle shift, explains ~23% of this change |
| [[RKO (line)]] | wt | 227 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.524× (z -9.8) ⚠ cell-cycle shift, explains ~23% of this change |
| [[SK-MEL-2 (line)]] | alt | 165 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.52× (z +9.3) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[SW48 (line)]] | wt | 164 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +10.7) ⚠ cell-cycle shift, explains ~74% of this change | — |
| [[A498 (line)]] | wt | 254 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 166 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 140 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 191 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 266 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 208 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 144 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 252 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 202 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 227 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 241 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 93.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 206 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 127 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 208 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 181 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 214 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 185 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 183), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPIG]] | +0.78 | +0.81 / +0.70 | both halves | 7e-06 |  |
| [[AKAP9]] | +0.77 | +0.79 / +0.71 | both halves | 7e-06 |  |
| [[PIGBOS1]] | +0.76 | +0.71 / +0.76 | both halves | 7e-06 |  |
| [[SRSF11]] ⚠ | +0.76 | +0.74 / +0.71 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[CCDC174]] | +0.75 | +0.78 / +0.74 | both halves | 7e-06 |  |
| [[SNW1]] | +0.73 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[RBMX2]] | +0.72 | +0.76 / +0.73 | both halves | 7e-06 |  |
| [[MRPS18B]] | +0.72 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[MRPS18C]] | +0.71 | +0.78 / +0.65 | both halves | 7e-06 |  |
| [[ITSN2]] | +0.71 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[MRFAP1L1]] | +0.70 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[COIL]] | +0.70 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[BOD1L1]] | +0.69 | +0.79 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKT1]] | -0.75 | -0.75 / -0.74 | both halves | 7e-06 |  |
| [[SLC25A39]] | -0.69 | -0.64 / -0.69 | both halves | 7e-06 |  |
| [[COLGALT1]] | -0.69 | -0.64 / -0.75 | both halves | 7e-06 |  |
| [[ADAM15]] | -0.66 | -0.60 / -0.68 | both halves | 7e-06 |  |
| [[MFSD14B]] | -0.66 | -0.67 / -0.64 | both halves | 7e-06 |  |
| [[RBBP7]] | -0.65 | -0.69 / -0.61 | both halves | 7e-06 |  |
| [[NAGA]] | -0.65 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[ACLY]] | -0.64 | -0.53 / -0.68 | both halves | 1e-05 |  |
| [[PRPS2]] | -0.64 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[NIPA2]] | -0.64 | -0.61 / -0.60 | both halves | 7e-06 |  |
| [[DHRS11]] | -0.63 | -0.59 / -0.58 | both halves | 7e-06 |  |
| [[SIGMAR1]] | -0.63 | -0.57 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SEC62's level | compounds that target TOP2A: 2 of 5 lower it (Doxorubicin, Idarubicin) | 40% of the class's compounds vs 0.6% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[WBP2NL]] | B | WBP2NL activity lowers SEC62's level | lines that do not express WBP2NL (17) vs lines expressing it (33) | 1.18× higher at baseline in the lines without WBP2NL | 0.091 | ⚠ within organs, on part of the lines; also absent: ATP2A3, GCNT2, ENSG00000235726; maybe low, not absent |
| [[DUSP15]] | B | DUSP15 activity weakens SEC62's drug response | lines that do not express DUSP15 (15) vs lines expressing it (34) | the lines without DUSP15 respond 1.24× as strongly (z diff -0.74); strongest at Ouabain (Octahydrate) 5 µM: 1.66x vs 1.37x (z diff -2.0) | 0.096 | ⚠ within organs, on part of the lines; also absent: DLK2, ETNK2, C11orf96; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.791). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-36.7, 1.7); signed map (-11.5, -5.2). **Vector** length 116, 46.0% of its response variance represented; |z| ≥ 3 in 734 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *mRNA Splicing - Major Pathway* (reactome, mean cos +0.54 to 17); *mRNA Splicing* (reactome, mean cos +0.54 to 17); *Processing of Capped Intron-Containing Pre-mRNA* (reactome, mean cos +0.52 to 19).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +8.6 | +9.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | +7.3 | +8.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.2 | +6.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.9 | +6.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +5.8 | +8.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +0.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.4 | +4.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.2 | +0.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.1 | +0.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.9 | -1.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -4.9 | -4.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -4.9 | -3.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -1.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | +1.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.4 | -1.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.4 | -1.5 |
|  | [[Clonidine (hydrochloride) (drug)]] 5 µM |  | -2.3 | -1.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.2 | +0.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.1 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | SEC62 preprotein translocation factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q26.2 — chr3:169,966,635-169,998,373 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Dtrp1, HTP1; previously TLOC1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99442](https://www.uniprot.org/uniprotkb/Q99442) (Translocation protein SEC62):

> Mediates post-translational transport of precursor polypeptides across endoplasmic reticulum (ER). Proposed to act as a targeting receptor for small presecretory proteins containing short and apolar signal peptides. Targets and properly positions newly synthesized presecretory proteins into the SEC61 channel-forming translocon complex, triggering channel opening for polypeptide translocation to the ER lumen.

**Summary**, from NCBI Gene [7095](https://www.ncbi.nlm.nih.gov/gene/7095):

> The Sec61 complex is the central component of the protein translocation apparatus of the endoplasmic reticulum (ER) membrane. The protein encoded by this gene and SEC63 protein are found to be associated with ribosome-free SEC61 complex. It is speculated that Sec61-Sec62-Sec63 may perform post-translational protein translocation into the ER. The Sec61-Sec62-Sec63 complex might also perform the backward transport of ER proteins that are subject to the ubiquitin-proteasome-dependent degradation …

**Accessions** — [HGNC:11846](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11846) · Entrez [7095](https://www.ncbi.nlm.nih.gov/gene/7095) · UniProt [Q99442](https://www.uniprot.org/uniprotkb/Q99442) · Ensembl [ENSG00000008952](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000008952)

## Data

Gene col 183: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 183); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 183, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 183]; `tensor/DDL_lfc|DDL_z.npy` [183]; `embed/gene_vectors.npy` [183]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 183 or target_col == 183). Every well: [[SEC62 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEC62.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
