---
symbol: "RP9"
type: "gene"
col: 8970
ensembl_id: "ENSG00000164610"
name: "RP9 pre-mRNA splicing factor"
location: "7p14.3"
module: 12
arm: "+"
pooled_cpm: 26.93
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 6
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# RP9

*RP9 pre-mRNA splicing factor* — 7p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.48× (z +10.5, q 5e-23, up in 47 of 48 measured lines) ⚠ cell-cycle shift, explains ~46% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 3.36× (z +9.9, q 1e-20, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.515× (z -5.4, q 2e-05, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C18orf21]] (+0.82, fdr 7e-06), [[RIOK2]] (+0.82, fdr 7e-06), [[EBAG9]] (+0.80, fdr 7e-06); moves opposite to [[HCFC1]] (-0.77, fdr 7e-06), [[PRDM10]] (-0.71, fdr 7e-06), [[ATP2A2]] (-0.64, fdr 7e-06).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[SLC25A12]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8970.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **2.48×** | +10.5 | 5e-23 | 47/48 (PANC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.36×** | +9.9 | 1e-20 | 47/48 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.87×** | +8.3 | 2e-14 | 46/48 (PANC-1, NCI-H460, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.73×** | +5.6 | 3e-06 | 44/48 (SW480, SW1417, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.28×** | +5.6 | 3e-06 | 37/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.88×** | +5.2 | 2e-05 | 36/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~56% of this change | **1.66×** | +4.1 | 0.003 | 32/47 (PANC-1, RPMI-7951, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.67×** | +4.0 | 0.004 | 26/47 (LoVo, PANC-1, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.15×** | +3.3 | 0.065 | 23/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.48×** | +3.2 | 0.068 | 28/48 (SNU-423, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.069 | 25/48 (LoVo, SNU-423, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | 1.45× | +3.1 | 0.10 | 23/48 (AsPC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8970.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.515×** | -5.4 | 2e-05 | 40/48 (KATO III, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.626×** | -5.4 | 2e-05 | 37/48 (AsPC-1, SW480, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.642×** | -5.1 | 7e-05 | 33/48 (HS-578T, HepG2/C3A, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.555×** | -4.8 | 2e-04 | 32/48 (KATO III, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.571×** | -4.4 | 0.001 | 32/47 (SW480, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.663×** | -3.3 | 0.081 | 25/48 (AsPC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 0.664× | -3.2 | 0.12 | 27/48 (SW480, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.63 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8970. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 26.0 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.31× (z +15.1) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.92× (z +10.4) | — |
| [[NCI-H2030 (line)]] | alt | 24.3 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.61× (z +13.1) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.61× (z +9.3) | — |
| [[NCI-H23 (line)]] | alt | 19.7 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +9.0) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.99× (z +8.6) | — |
| [[NCI-H2347 (line)]] | alt | 23.4 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +9.0) ⚠ cell-cycle shift, explains ~46% of this change | [[Dinaciclib (drug)]] 5 µM 0.212× (z -10.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 25.4 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.07× (z +15.3) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.11× (z +10.9) | — |
| [[HEC-1-A (line)]] | alt | 34.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +11.9) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.57× (z +9.9) | — |
| [[KATO III (line)]] | alt | 41.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +10.7) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.01× (z +8.6) | — |
| [[NCI-H460 (line)]] | wt | 22.8 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 5.56× (z +10.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.30× (z +9.4) | — |
| [[A-427 (line)]] | wt | 22.6 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.82× (z +8.5) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[AsPC-1 (line)]] | alt | 15.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -9.8) |
| [[C32 (line)]] | wt | 31.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0487× (z -11.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 18.4 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0540× (z -11.8) |
| [[HT-29 (line)]] | alt | 18.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +8.7) ⚠ cell-cycle shift, explains ~46% of this change | — |
| [[LoVo (line)]] | wt | 24.9 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.54× (z +8.9) | — |
| [[LOX-IMVI (line)]] | wt | 17.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +8.5) ⚠ cell-cycle shift, explains ~46% of this change | — |
| [[LS 180 (line)]] | wt | 25.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.93× (z +9.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 21.5 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.13× (z +10.2) | — |
| [[NCI-H1792 (line)]] | alt | 17.3 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.34× (z +8.7) | — |
| [[RPMI-7951 (line)]] | alt | 35.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.306× (z -8.9) |
| [[SW48 (line)]] | wt | 35.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +9.8) ⚠ cell-cycle shift, explains ~46% of this change | — |
| [[SW480 (line)]] | alt | 53.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -9.5) |
| [[A-172 (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 45.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8970), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C18orf21]] | +0.82 | +0.77 / +0.82 | both halves | 7e-06 |  |
| [[RIOK2]] | +0.82 | +0.84 / +0.74 | both halves | 7e-06 |  |
| [[EBAG9]] | +0.80 | +0.85 / +0.78 | both halves | 7e-06 |  |
| [[ZNF205]] | +0.79 | +0.78 / +0.70 | both halves | 7e-06 |  |
| [[PHAX]] | +0.78 | +0.84 / +0.79 | both halves | 7e-06 |  |
| [[RBMX2]] | +0.78 | +0.73 / +0.75 | both halves | 7e-06 | STRING 426 |
| [[SNHG11]] | +0.78 | +0.72 / +0.77 | both halves | 7e-06 |  |
| [[ASB8]] | +0.76 | +0.74 / +0.76 | both halves | 7e-06 |  |
| [[KBTBD7]] | +0.74 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[FAM133B]] | +0.74 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[MRPS31]] | +0.74 | +0.75 / +0.76 | both halves | 7e-06 |  |
| [[TARS2]] | +0.73 | +0.68 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HCFC1]] | -0.77 | -0.77 / -0.71 | both halves | 7e-06 |  |
| [[PRDM10]] | -0.71 | -0.81 / -0.58 | both halves | 7e-06 |  |
| [[ATP2A2]] | -0.64 | -0.58 / -0.69 | both halves | 7e-06 |  |
| [[CERS2]] | -0.64 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[PRPS2]] | -0.63 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[MOB1A]] | -0.63 | -0.48 / -0.62 | both halves | 2e-05 |  |
| [[EIF4EBP2]] | -0.63 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[TARDBP]] | -0.62 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[M6PR]] | -0.62 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[C2CD3]] | -0.62 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[CDK2]] | -0.62 | -0.68 / -0.55 | both halves | 1e-05 |  |
| [[SUMO3]] | -0.62 | -0.50 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises RP9's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 1.4% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity raises RP9's level | compounds that target TOP2B: 2 of 2 lower it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC25A12]] | C | RP9's natural level weakens SLC25A12's drug response | RP9's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.68, reverse +0.06; direction not clear | 0.016 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.864). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-38.0, -8.7); signed map (-15.7, -8.7). **Vector** length 127, 44.1% of its response variance represented; |z| ≥ 3 in 692 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.5 | +9.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +8.3 | +10.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +7.7 | +8.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.6 | +5.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.1 | +5.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +5.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.6 | +1.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.4 | +3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +3.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.1 | +1.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -9.7 | -5.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -9.2 | -4.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -8.1 | -3.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.8 | -5.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -7.1 | -2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.0 | -5.1 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -2.0 | -2.5 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.8 | -1.7 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.7 | -2.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.6 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | RP9 pre-mRNA splicing factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.3 — chr7:33,094,797-33,109,405 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PAP-1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TA86](https://www.uniprot.org/uniprotkb/Q8TA86) (Retinitis pigmentosa 9 protein):

> Is thought to be a target protein for the PIM1 kinase. May play some roles in B-cell proliferation in association with PIM1 (By similarity).

**Summary**, from NCBI Gene [6100](https://www.ncbi.nlm.nih.gov/gene/6100):

> The protein encoded by this gene can be bound and phosphorylated by the protooncogene PIM1 product, a serine/threonine protein kinase . This protein localizes in nuclear speckles containing the splicing factors, and has a role in pre-mRNA splicing. CBF1-interacting protein (CIR), a corepressor of CBF1, can also bind to this protein and effects alternative splicing. Mutations in this gene result in autosomal dominant retinitis pigmentosa-9. This gene has a pseudogene (GeneID: 441212), which is …

**Accessions** — [HGNC:10288](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10288) · Entrez [6100](https://www.ncbi.nlm.nih.gov/gene/6100) · UniProt [Q8TA86](https://www.uniprot.org/uniprotkb/Q8TA86) · Ensembl [ENSG00000164610](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164610)

## Data

Gene col 8970: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8970); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8970, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8970]; `tensor/DDL_lfc|DDL_z.npy` [8970]; `embed/gene_vectors.npy` [8970]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8970 or target_col == 8970). Every well: [[RP9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RP9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
