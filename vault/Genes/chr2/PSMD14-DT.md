---
symbol: "PSMD14-DT"
type: "gene"
col: 14034
ensembl_id: "ENSG00000235724"
name: "PSMD14 divergent transcript"
location: "2q24.2"
module: 35
arm: "+"
pooled_cpm: 3.5
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 0
n_dd_up_clean: 25
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# PSMD14-DT

*PSMD14 divergent transcript* — 2q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.99× (z +25.4, q 0e+00, up in 38 of 38 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP1R42]] (+0.85, fdr 7e-06), [[INTS6-AS1]] (+0.83, fdr 7e-06), [[ATE1OSP]] (+0.81, fdr 7e-06).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CBX2]] → it (grade B ⚠); 1 goes from it, the strongest it → [[TSTD3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14034.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.99×** | +25.4 | 0e+00 | 38/38 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.77×** | +13.7 | 2e-40 | 6/6 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.36×** | +13.6 | 1e-39 | 31/37 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.37×** | +13.0 | 9e-37 | 3/4 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.81×** | +11.5 | 9e-29 | 18/21 (SW480, A549, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.54×** | +10.4 | 2e-23 | 29/43 (NCI-H23, C32, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.47×** | +9.7 | 2e-20 | 23/32 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.40×** | +9.4 | 4e-19 | 25/36 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.07×** | +7.8 | 3e-13 | 12/18 (NCI-H1573, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.87×** | +7.0 | 1e-10 | 19/37 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.84×** | +6.8 | 5e-10 | 10/21 (NCI-H1573, NCI-H460, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.84×** | +6.8 | 5e-10 | 18/43 (HEC-1-A, C32, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.47×** | +6.1 | 5e-08 | 9/45 (A498, RKO, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.71×** | +5.8 | 3e-07 | 18/43 (NCI-H23, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.55×** | +4.9 | 4e-05 | 13/45 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.47×** | +4.3 | 5e-04 | 14/42 (A498, A-172, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.45×** | +3.9 | 0.003 | 2/43 (NCI-H2347, PANC-1) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.42×** | +3.9 | 0.003 | 12/46 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.40×** | +3.8 | 0.005 | 4/45 (HEC-1-A, LS 180, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.41×** | +3.7 | 0.006 | 3/39 (A-172, HOP62, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14034.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | 0.733× | -3.5 | 0.17 | 4/46 (PANC-1, KATO III, …) | rises with dose | position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.807× | -3.4 | 0.17 | 7/46 (NCI-H1573, SW48, …) | rises with dose | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.919× | -3.3 | 0.17 | 14/48 (C32, HEC-1-A, …) | inconsistent across doses |  |
| [[Hesperidin (drug)]] 0.05 µM |  | 0.741× | -3.1 | 0.25 | 7/43 (C-33 A, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14034. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 4.31 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 11.7× (z +11.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.44× (z +8.9) | — |
| [[A549 (line)]] | wt | 3.32 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 16.6× (z +9.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.29× (z +9.1) | — |
| [[NCI-H2030 (line)]] | alt | 3.16 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.74× (z +10.7) | — |
| [[A-172 (line)]] | wt | 3.72 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.69× (z +9.5) | — |
| [[A498 (line)]] | wt | 4.85 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.71× (z +9.8) | — |
| [[AsPC-1 (line)]] | alt | 2.55 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.48× (z +8.5) | — |
| [[HEC-1-A (line)]] | alt | 5.52 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.85× (z +10.9) | — |
| [[HOP62 (line)]] | alt | 4.27 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.49× (z +10.8) | — |
| [[HS-578T (line)]] | alt | 2.74 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.57× (z +9.4) | — |
| [[LOX-IMVI (line)]] | wt | 3.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.25× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 3.00 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.32× (z +8.7) | — |
| [[NCI-H23 (line)]] | alt | 4.27 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.9× (z +11.5) | — |
| [[NCI-H460 (line)]] | wt | 3.43 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.52× (z +9.6) | — |
| [[PANC-1 (line)]] | alt | 3.80 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.49× (z +13.6) | — |
| [[SW 900 (line)]] | alt | 3.53 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.37× (z +9.0) | — |
| [[A-427 (line)]] | wt | 4.74 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.94 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.58 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.85 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14034), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R42]] | +0.85 | +0.81 / +0.73 | both halves | 7e-06 |  |
| [[INTS6-AS1]] | +0.83 | +0.80 / +0.68 | both halves | 7e-06 |  |
| [[ATE1OSP]] | +0.81 | +0.78 / +0.66 | both halves | 7e-06 |  |
| [[H2AZ1-DT]] | +0.80 | +0.84 / +0.61 | both halves | 7e-06 | same gene group |
| [[LRRC8C-DT]] | +0.80 | +0.74 / +0.63 | both halves | 7e-06 | same gene group |
| [[DENND6A-AS1]] | +0.80 | +0.82 / +0.58 | both halves | 7e-06 |  |
| [[LANCL1-AS1]] | +0.79 | +0.71 / +0.77 | both halves | 7e-06 |  |
| [[SPATA1]] | +0.79 | +0.74 / +0.71 | both halves | 7e-06 |  |
| [[LINC01090]] | +0.79 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[CARNMT1-AS1]] | +0.77 | +0.69 / +0.77 | both halves | 7e-06 |  |
| [[TMEM202-AS1]] | +0.77 | +0.76 / +0.61 | both halves | 7e-06 |  |
| [[USP38-DT]] | +0.77 | +0.76 / +0.63 | both halves | 7e-06 | same gene group |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CBX2]] | B | CBX2 activity raises PSMD14-DT's level | lines that do not express CBX2 (6) vs lines expressing it (44) | 1.35× lower at baseline in the lines without CBX2 | 0.001 | ⚠ within organs, on part of the lines; also absent: CCNP, CTXN1, ADGRL1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers PSMD14-DT's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 7.0% of all compounds | 0.009 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[GREB1]] | B | GREB1 activity raises PSMD14-DT's level | lines that do not express GREB1 (6) vs lines expressing it (44) | 1.28× lower at baseline in the lines without GREB1 | 0.024 | ⚠ within organs, on part of the lines; also absent: PRKN, SLC17A7, ENSG00000232855; maybe low, not absent |
| [[JAK2]] | B | JAK2 activity lowers PSMD14-DT's level | compounds that target JAK2: 3 of 3 raise it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 7.0% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSTD3]] | C | PSMD14-DT's natural level strengthens TSTD3's drug response | PSMD14-DT's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.08; direction not clear | 0.086 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.815). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (11.4, 22.7); signed map (29.8, -0.8). **Vector** length 56.3, 7.61% of its response variance represented; |z| ≥ 3 in 945 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.7 | +25.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +13.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +13.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +11.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +10.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +4.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.2 | +3.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.7 | +2.0 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | +2.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | +0.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.7 | +3.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | +2.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -1.5 | +3.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | +0.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.2 | -1.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.2 | -3.4 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | PSMD14 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2q24.2 — chr2:161,222,785-161,308,389 (-) |
| Ensembl biotype | lncRNA |
| Also known as | uc.88 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:56104](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:56104) · Entrez [101929512](https://www.ncbi.nlm.nih.gov/gene/101929512) · Ensembl [ENSG00000235724](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000235724)

## Data

Gene col 14034: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14034); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14034, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14034]; `tensor/DDL_lfc|DDL_z.npy` [14034]; `embed/gene_vectors.npy` [14034]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14034 or target_col == 14034). Every well: [[PSMD14-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMD14-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
