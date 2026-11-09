---
symbol: "ADAMTS9-AS2"
type: "gene"
col: 14282
ensembl_id: "ENSG00000241684"
name: "ADAMTS9 antisense RNA 2"
location: "3p14.1"
module: 13
arm: "+"
pooled_cpm: 31.37
n_lines_expressing: 20
n_dd_up: 10
n_dd_down: 17
n_dd_up_clean: 8
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 18
direction_downstream: 31
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# ADAMTS9-AS2

*ADAMTS9 antisense RNA 2* — 3p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.38× (z +15.6, q 0e+00, up in 6 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.527× (z -8.2, q 2e-13, down in 15 of 18 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EFCAB13]] (+0.64, fdr 7e-06), [[IQCA1]] (+0.62, fdr 1e-05), [[LINC02882]] (+0.62, fdr 3e-05); moves opposite to [[TARBP1]] (-0.50, fdr 3e-05), [[REV1]] (-0.45, fdr 4e-05), [[ZFAND4]] (-0.44, fdr 7e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[THEMIS2]] → it (grade B ⚠); 31 go from it, the strongest it → [[THEMIS2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14282.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.38×** | +15.6 | 0e+00 | 6/18 (HEC-1-A, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.91×** | +8.2 | 5e-14 | 1/18 (H4) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +6.6 | 8e-09 | 1/16 (H4) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +5.6 | 2e-06 | 9/18 (SNU-423, NCI-H2347, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +4.2 | 0.002 | 0/18 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.41×** | +4.2 | 0.002 | 0/18 | top dose only | position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.34×** | +3.7 | 0.015 | 0/18 | inconsistent across doses | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +3.7 | 0.018 | 3/18 (HEC-1-A, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.094 | 4/17 (Panc 03.27, A498, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.094 | 2/18 (SW 1088, CHP-212) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14282.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.527×** | -8.2 | 2e-13 | 15/18 (CFPAC-1, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.654×** | -7.7 | 4e-12 | 15/18 (CFPAC-1, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~11% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.549×** | -7.6 | 4e-12 | 18/18 (RPMI-7951, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.567×** | -7.2 | 6e-11 | 17/18 (CFPAC-1, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.656×** | -5.4 | 9e-06 | 16/18 (HOP62, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.493×** | -4.7 | 2e-04 | 15/18 (RPMI-7951, HOP62, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.714×** | -4.1 | 0.003 | 13/17 (RPMI-7951, CFPAC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.738×** | -3.9 | 0.007 | 8/18 (A549, SW 900, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.738×** | -3.9 | 0.007 | 13/18 (SW 900, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **0.748×** | -3.6 | 0.020 | 7/18 (CHP-212, SW 900, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.757×** | -3.6 | 0.020 | 9/18 (CFPAC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.750×** | -3.5 | 0.020 | 16/18 (CFPAC-1, HOP62, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.769×** | -3.4 | 0.035 | 15/18 (RPMI-7951, HOP62, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.770×** | -3.3 | 0.035 | 2/18 (NCI-H1792, HOP62) | inconsistent across doses |  |
| [[Allopurinol (drug)]] 0.05 µM |  | **0.779×** | -3.2 | 0.054 | 4/18 (A549, SK-MEL-2, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.622×** | -3.2 | 0.054 | 8/18 (Panc 03.27, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.842× | -3.1 | 0.063 | 10/18 (CHP-212, C32, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | **0.792×** | -3.0 | 0.090 | 3/18 (HOP62, NCI-H1573, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14282. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 219 | 0 | 14 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0708× (z -23.3) |
| [[SW 900 (line)]] | alt | 137 | 0 | 12 (9 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.104× (z -15.1) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.243× (z -9.5) |
| [[HOP62 (line)]] | alt | 194 | 0 | 11 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0982× (z -21.7) |
| [[Panc 03.27 (line)]] | alt | 168 | 0 | 11 (9 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.116× (z -16.2) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.226× (z -11.2) |
| [[RPMI-7951 (line)]] | alt | 187 | 0 | 11 (9 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0583× (z -18.7) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.158× (z -17.1) |
| [[CHP-212 (line)]] | wt | 340 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0140× (z -25.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -9.7) |
| [[SK-MEL-2 (line)]] | alt | 51.2 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0744× (z -22.2) |
| [[C32 (line)]] | wt | 51.4 | 0 | 3 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.155× (z -9.6) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.193× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 19.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.137× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.275× (z -10.1) |
| [[H4 (line)]] | wt | 26.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0429× (z -12.9) |
| [[SNU-423 (line)]] | alt | 30.2 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.167× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 21.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.125× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 10.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.84× (z +10.5) | — |
| [[NCI-H1792 (line)]] | alt | 20.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -8.8) |
| [[A-172 (line)]] | wt | 3.13 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.15 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.14 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.02 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.43 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.27 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.56 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.93 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.76 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.94 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.25 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.80 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.67 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.22 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.85 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.76 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.20 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.86 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.06 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.53 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.40 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.38 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.33 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 5.34 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.37 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.24 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14282), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFCAB13]] | +0.64 | +0.59 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[IQCA1]] | +0.62 | +0.56 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[LINC02882]] | +0.62 | +0.65 / +0.45 | both halves | 3e-05 | **novel candidate** |
| [[ST8SIA6-AS1]] | +0.60 | +0.42 / +0.58 | both halves | 4e-05 | same gene group |
| [[MAGI2]] | +0.58 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[OR9Q1]] | +0.56 | +0.66 / +0.42 | both halves | 4e-05 |  |
| [[DNAH11]] | +0.55 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[SETBP1]] | +0.54 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[CP]] | +0.54 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[WFDC10B]] | +0.53 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[ADAM12]] | +0.53 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[SLC16A6]] | +0.53 | +0.51 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TARBP1]] | -0.50 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[REV1]] | -0.45 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[ZFAND4]] | -0.44 | -0.42 / -0.38 | both halves | 7e-05 |  |
| [[GK5]] | -0.43 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[GNPTAB]] | -0.42 | -0.23 / -0.51 | both halves | 5e-04 |  |
| [[ALG6]] | -0.41 | -0.36 / -0.45 | both halves | 9e-05 |  |
| [[ZNF18]] | -0.41 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[SSX2IP]] | -0.40 | -0.36 / -0.43 | both halves | 9e-05 |  |
| [[DCAF17]] | -0.40 | -0.39 / -0.47 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 3, C 15. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[THEMIS2]] | B | THEMIS2 activity raises ADAMTS9-AS2's level | lines that do not express THEMIS2 (19) vs lines expressing it (31) | 3.01× lower at baseline in the lines without THEMIS2 | 0.055 | ⚠ within organs, on part of the lines; also absent: TNFRSF9, PLAU, IGDCC4 |
| [[WFDC10B]] | B | WFDC10B activity raises ADAMTS9-AS2's level | lines that do not express WFDC10B (20) vs lines expressing it (30) | 2.28× lower at baseline in the lines without WFDC10B | 0.058 | ⚠ within organs, on part of the lines; also absent: WFDC3, QPCT, LRRN1; maybe low, not absent |
| [[ZNF439]] | B | ZNF439 activity raises ADAMTS9-AS2's level | lines that do not express ZNF439 (21) vs lines expressing it (29) | 2.55× lower at baseline in the lines without ZNF439 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000267383, PPP2R2B, CSF1R |
| [[SHROOM4]] | C | SHROOM4 activity raises ADAMTS9-AS2's level | lines that do not express SHROOM4 (30) vs lines expressing it (20) | 4.23× lower at baseline in the lines without SHROOM4 | 0.004 | ⚠ within organs, on part of the lines; also absent: CX3CL1, CD74, ENSG00000233539; co-absent with the target |
| [[BICC1]] | C | BICC1 activity raises ADAMTS9-AS2's level | lines that do not express BICC1 (28) vs lines expressing it (22) | 5.64× lower at baseline in the lines without BICC1 | 0.005 | ⚠ within organs, on part of the lines; also absent: ITGB3, COL4A1, COL4A2; co-absent with the target |
| [[EDNRA]] | C | EDNRA activity raises ADAMTS9-AS2's level | lines that do not express EDNRA (32) vs lines expressing it (18) | 6.09× lower at baseline in the lines without EDNRA | 0.005 | ⚠ within organs, on part of the lines; also absent: CCBE1, G0S2, ADAMTS12; co-absent with the target |
| [[MAF]] | C | MAF activity raises ADAMTS9-AS2's level | lines that do not express MAF (27) vs lines expressing it (23) | 4.58× lower at baseline in the lines without MAF | 0.007 | ⚠ within organs, on part of the lines; also absent: TNFAIP6, PLPP4, FN1; co-absent with the target |
| [[ITGB3]] | C | ITGB3 activity raises ADAMTS9-AS2's level | lines that do not express ITGB3 (25) vs lines expressing it (25) | 5.17× lower at baseline in the lines without ITGB3 | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, BICC1, ENSG00000291130; co-absent with the target |
| [[MILR1]] | C | MILR1 activity raises ADAMTS9-AS2's level | lines that do not express MILR1 (19) vs lines expressing it (31) | 3.22× lower at baseline in the lines without MILR1 | 0.009 | ⚠ within organs, on part of the lines; also absent: EVA1A, LINC00973, NLRP1; co-absent with the target |
| [[IGFBP7]] | C | IGFBP7 activity raises ADAMTS9-AS2's level | lines that do not express IGFBP7 (27) vs lines expressing it (23) | 3.94× lower at baseline in the lines without IGFBP7 | 0.011 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, FN1; co-absent with the target |
| [[LOX]] | C | LOX activity raises ADAMTS9-AS2's level | lines that do not express LOX (31) vs lines expressing it (19) | 4.72× lower at baseline in the lines without LOX | 0.018 | ⚠ within organs, on part of the lines; also absent: C5orf46, RRAD, LINC01411; co-absent with the target |
| [[IGFBP3]] | C | IGFBP3 activity raises ADAMTS9-AS2's level | lines that do not express IGFBP3 (20) vs lines expressing it (30) | 4.83× lower at baseline in the lines without IGFBP3 | 0.019 | ⚠ within organs, on part of the lines; also absent: ADRA1B, ADAM12, MAF; co-absent with the target |

### Downstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 14, C 17. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[THEMIS2]] | B | ADAMTS9-AS2 activity raises THEMIS2's level | lines that do not express ADAMTS9-AS2 (30) vs lines expressing it (20) | 3.37× lower at baseline in the lines without ADAMTS9-AS2 | 0.004 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ENSG00000233539, NID2 |
| [[DCAF17]] | B | ADAMTS9-AS2 activity lowers DCAF17's level | lines that do not express ADAMTS9-AS2 (30) vs lines expressing it (20) | 1.31× higher at baseline in the lines without ADAMTS9-AS2 | 0.005 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ENSG00000233539, NID2 |
| [[NR2F2-AS1]] | B | ADAMTS9-AS2 activity raises NR2F2-AS1's level | lines that do not express ADAMTS9-AS2 (30) vs lines expressing it (20) | 2.98× lower at baseline in the lines without ADAMTS9-AS2 | 0.019 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ENSG00000233539, NID2 |
| [[LINC01239]] | B | ADAMTS9-AS2 activity raises LINC01239's level | lines that do not express ADAMTS9-AS2 (30) vs lines expressing it (20) | 3.08× lower at baseline in the lines without ADAMTS9-AS2 | 0.030 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ENSG00000233539, NID2 |
| [[SSX2IP]] | B | ADAMTS9-AS2 activity lowers SSX2IP's level | lines that do not express ADAMTS9-AS2 (30) vs lines expressing it (20) | 1.68× higher at baseline in the lines without ADAMTS9-AS2 | 0.044 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ENSG00000233539, NID2 |
| [[EFCAB13]] | B | ADAMTS9-AS2 activity raises EFCAB13's level | lines that do not express ADAMTS9-AS2 (30) vs lines expressing it (20) | 3.12× lower at baseline in the lines without ADAMTS9-AS2 | 0.045 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ENSG00000233539, NID2 |
| [[ESR2]] | B | ADAMTS9-AS2 activity raises ESR2's level | lines that do not express ADAMTS9-AS2 (30) vs lines expressing it (20) | 1.31× lower at baseline in the lines without ADAMTS9-AS2 | 0.051 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ENSG00000233539, NID2 |
| [[NRP1]] | B | ADAMTS9-AS2 activity raises NRP1's level | lines that do not express ADAMTS9-AS2 (30) vs lines expressing it (20) | 3.14× lower at baseline in the lines without ADAMTS9-AS2 | 0.052 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ENSG00000233539, NID2 |
| [[ESR2]] | B | ADAMTS9-AS2 activity weakens ESR2's drug response | lines that do not express ADAMTS9-AS2 (30) vs lines expressing it (18) | the lines without ADAMTS9-AS2 respond 1.58× as strongly (z diff -1.09); strongest at Dinaciclib 0.05 µM: 1.71x vs 0.90x (z diff -3.0) | 0.056 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ENSG00000233539, NID2; target measured in part of the lines; artifact flags |
| [[LINC00536]] | B | ADAMTS9-AS2 activity raises LINC00536's level | lines that do not express ADAMTS9-AS2 (30) vs lines expressing it (20) | 2.47× lower at baseline in the lines without ADAMTS9-AS2 | 0.064 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ENSG00000233539, NID2 |
| [[TARBP1]] | B | ADAMTS9-AS2 activity lowers TARBP1's level | lines that do not express ADAMTS9-AS2 (30) vs lines expressing it (20) | 1.52× higher at baseline in the lines without ADAMTS9-AS2 | 0.065 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ENSG00000233539, NID2 |
| [[FAM20C]] | B | ADAMTS9-AS2 activity raises FAM20C's level | lines that do not express ADAMTS9-AS2 (30) vs lines expressing it (20) | 3.57× lower at baseline in the lines without ADAMTS9-AS2 | 0.087 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ENSG00000233539, NID2 |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.428). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.0, 23.9); signed map (31.1, 48.7). **Vector** length 83.1, 31.2% of its response variance represented; |z| ≥ 3 in 561 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.0 | +15.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +8.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.5 | +5.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.3 | +1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +2.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.1 | +1.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.8 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | -1.3 |
| fall | [[Brivudine (drug)]] 5 µM |  | -2.5 | -4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -1.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.0 | -1.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -3.3 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -1.8 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | ADAMTS9 antisense RNA 2 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3p14.1 — chr3:64,684,909-65,053,439 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100507098](https://www.ncbi.nlm.nih.gov/gene/100507098):

> Implicated in diabetic retinopathy. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:42435](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:42435) · Entrez [100507098](https://www.ncbi.nlm.nih.gov/gene/100507098) · Ensembl [ENSG00000241684](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000241684)

## Data

Gene col 14282: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14282); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14282, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14282]; `tensor/DDL_lfc|DDL_z.npy` [14282]; `embed/gene_vectors.npy` [14282]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14282 or target_col == 14282). Every well: [[ADAMTS9-AS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADAMTS9-AS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
