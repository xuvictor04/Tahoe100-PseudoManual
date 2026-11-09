---
symbol: "UBE2B"
type: "gene"
col: 4039
ensembl_id: "ENSG00000119048"
name: "ubiquitin conjugating enzyme E2 B"
location: "5q31.1"
module: 74
arm: "+"
pooled_cpm: 195.06
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 3
n_dd_up_clean: 3
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# UBE2B

*ubiquitin conjugating enzyme E2 B* — 5q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.59× (z +6.9, q 3e-09, up in 37 of 48 measured lines) ⚠ cell-cycle shift, explains ~49% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.56× (z +4.7, q 8e-04, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.697× (z -5.3, q 4e-05, down in 38 of 49 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.792× (z -3.4, q 0.080, down in 32 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (CFPAC-1 0.474×, NCI-H1792 0.478×, SNU-423 0.537×; ⚠ cell-cycle shift, explains ~26% of this change); [[c-Kit-IN-1 (drug)]] 0.05 µM in 2 lines (AsPC-1 0.381×, NCI-H2347 0.455×; ⚠ unreliable plate only).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HDAC5]] (+0.76, fdr 7e-06), [[GABARAPL2]] (+0.73, fdr 7e-06), [[CAMLG]] (+0.72, fdr 7e-06); moves opposite to [[PSME3]] (-0.76, fdr 7e-06), [[SUV39H2]] (-0.73, fdr 7e-06), [[EMC1]] (-0.71, fdr 7e-06).
> It is in [[Module 074]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HENMT1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4039.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.59×** | +6.9 | 3e-09 | 37/48 (NCI-H460, COLO 205, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +4.7 | 8e-04 | 38/48 (AN3 CA, RKO, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.40×** | +3.6 | 0.069 | 33/48 (KATO III, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.39×** | +3.5 | 0.069 | 34/48 (HOP62, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.55× | +3.3 | 0.11 | 41/48 (LS 180, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | 1.35× | +3.2 | 0.13 | 27/48 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.23× | +3.1 | 0.14 | 30/49 (KATO III, Panc 03.27, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | 1.34× | +3.1 | 0.14 | 30/48 (LOX-IMVI, HS-578T, …) | two highest doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4039.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (CFPAC-1 0.474×, NCI-H1792 0.478×, SNU-423 0.537×; ⚠ cell-cycle shift, explains ~26% of this change); [[c-Kit-IN-1 (drug)]] 0.05 µM in 2 lines (AsPC-1 0.381×, NCI-H2347 0.455×; ⚠ unreliable plate only).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.697×** | -5.3 | 4e-05 | 38/49 (CFPAC-1, NCI-H1792, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.604×** | -5.3 | 4e-05 | 46/48 (AsPC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.908× | -3.5 | 0.080 | 0/50 | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.792×** | -3.4 | 0.080 | 32/48 (COLO 205, CFPAC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4039. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 230 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +13.1) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[NCI-H460 (line)]] | wt | 154 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +16.5) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[BT-474 (line)]] | alt | 122 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.11× (z +9.8) | — |
| [[RKO (line)]] | wt | 159 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.21× (z +9.9) | — |
| [[AN3 CA (line)]] | alt | 246 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.00× (z +11.3) | — |
| [[AsPC-1 (line)]] | alt | 332 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.381× (z -9.9) ⚠ unreliable plate only |
| [[C32 (line)]] | wt | 106 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.90× (z +8.5) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[CFPAC-1 (line)]] | alt | 311 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -10.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[COLO 205 (line)]] | alt | 254 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +15.2) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[J82 (line)]] | alt | 146 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +10.9) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[LS 180 (line)]] | wt | 224 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +8.9) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[NCI-H1792 (line)]] | alt | 209 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -10.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H2347 (line)]] | alt | 271 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.455× (z -9.2) ⚠ unreliable plate only |
| [[SNU-1 (line)]] | wt | 154 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +8.5) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[SNU-423 (line)]] | alt | 286 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.537× (z -8.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A-172 (line)]] | wt | 218 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 221 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 184 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 141 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 110 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 199 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 177 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 215 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 174 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 201 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 231 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 196 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 297 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 152 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 207 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 199 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 153 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 237 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 255 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 208 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 242 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 237 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 200 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 259 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 181 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 180 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4039), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDAC5]] | +0.76 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[GABARAPL2]] | +0.73 | +0.59 / +0.79 | both halves | 7e-06 |  |
| [[CAMLG]] | +0.72 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[SNHG7]] | +0.71 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[TBC1D17]] | +0.71 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[PGPEP1]] | +0.71 | +0.58 / +0.72 | both halves | 7e-06 |  |
| [[RPAIN]] | +0.70 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[SMIM26]] ⚠ | +0.70 | +0.67 / +0.65 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[ZCRB1]] | +0.69 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[UBXN1]] | +0.69 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[INAFM1]] | +0.68 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[SAT2]] | +0.68 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[ZFAND2B]] | +0.68 | +0.69 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSME3]] | -0.76 | -0.68 / -0.74 | both halves | 7e-06 |  |
| [[SUV39H2]] | -0.73 | -0.66 / -0.73 | both halves | 7e-06 |  |
| [[EMC1]] | -0.71 | -0.63 / -0.76 | both halves | 7e-06 |  |
| [[WDR77]] | -0.69 | -0.68 / -0.66 | both halves | 7e-06 |  |
| [[EIF5A]] | -0.69 | -0.74 / -0.61 | both halves | 7e-06 |  |
| [[ABCF2]] | -0.68 | -0.62 / -0.66 | both halves | 7e-06 |  |
| [[HCFC1]] | -0.67 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[NUP188]] | -0.67 | -0.56 / -0.74 | both halves | 1e-05 |  |
| [[SIGMAR1]] | -0.66 | -0.67 / -0.69 | both halves | 7e-06 |  |
| [[EIF4G1]] | -0.66 | -0.56 / -0.67 | both halves | 1e-05 |  |
| [[SUMO3]] | -0.66 | -0.60 / -0.55 | both halves | 1e-05 | STRING 415 |
| [[PIGW]] | -0.66 | -0.60 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HENMT1]] | B | HENMT1 activity raises UBE2B's level | lines that do not express HENMT1 (17) vs lines expressing it (33) | 1.12× lower at baseline in the lines without HENMT1 | 0.008 | ⚠ within organs, on part of the lines; also absent: SLC16A5, RPP25, ENSG00000267748 |
| [[TPST1]] | B | TPST1 activity lowers UBE2B's level | lines that do not express TPST1 (5) vs lines expressing it (45) | 1.39× higher at baseline in the lines without TPST1 | 0.045 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CYP46A1, CSRP2, MYO5A |
| [[CSTB]] | B | CSTB activity raises UBE2B's level | lines that do not express CSTB (8) vs lines expressing it (42) | 1.42× lower at baseline in the lines without CSTB | 0.097 | ⚠ within organs, on part of the lines; also absent: PLAUR, PLS3, ADGRE5; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.758). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.3, -48.1); signed map (-16.5, 5.7). **Vector** length 145, 59.3% of its response variance represented; |z| ≥ 3 in 607 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +6.9 | +6.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.2 | +4.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.6 | +3.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.4 | +3.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | +2.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +4.0 | +3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +1.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +3.6 | +2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.5 | +3.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -9.7 | -5.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -7.6 | -5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.8 | -3.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.6 | -2.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.3 | -2.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.9 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.7 | -1.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.2 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin conjugating enzyme E2 B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.1 — chr5:134,371,184-134,392,108 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UBC2, HHR6B, RAD6B |
| Gene groups (HGNC) | Ubiquitin conjugating enzymes E2 |
| Reactome | 9 pathways, smallest: Recognition of DNA damage by PCNA-containing replication complex; Synthesis of active ubiquitin: roles of E1 and E2 enzymes; DNA Damage Bypass |
| Matched by | ensembl_id |

**Function**, from UniProt [P63146](https://www.uniprot.org/uniprotkb/P63146) (Ubiquitin-conjugating enzyme E2 B):

> E2 ubiquitin-conjugating enzyme that accepts ubiquitin from the ubiquitin-activating enzyme E1 and transfers it to a E3 ubiquitin-protein ligase. In vitro catalyzes 'Lys-11'-, as well as 'Lys-48'- and 'Lys-63'-linked polyubiquitination. Together with the E3 enzyme BRE1 (RNF20 and/or RNF40), plays a role in transcription regulation by catalyzing the monoubiquitination of histone H2B at 'Lys-120' to form H2BK120ub1. H2BK120ub1 gives a specific tag for epigenetic transcriptional activation, …

**Summary**, from NCBI Gene [7320](https://www.ncbi.nlm.nih.gov/gene/7320):

> The modification of proteins with ubiquitin is an important cellular mechanism for targeting abnormal or short-lived proteins for degradation. Ubiquitination involves at least three classes of enzymes: ubiquitin-activating enzymes, or E1s, ubiquitin-conjugating enzymes, or E2s, and ubiquitin-protein ligases, or E3s. This gene encodes a member of the E2 ubiquitin-conjugating enzyme family. This enzyme is required for post-replicative DNA damage repair. Its protein sequence is 100% identical to …

**Accessions** — [HGNC:12473](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12473) · Entrez [7320](https://www.ncbi.nlm.nih.gov/gene/7320) · UniProt [P63146](https://www.uniprot.org/uniprotkb/P63146) · Ensembl [ENSG00000119048](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119048)

## Data

Gene col 4039: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4039); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4039, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4039]; `tensor/DDL_lfc|DDL_z.npy` [4039]; `embed/gene_vectors.npy` [4039]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4039 or target_col == 4039). Every well: [[UBE2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
