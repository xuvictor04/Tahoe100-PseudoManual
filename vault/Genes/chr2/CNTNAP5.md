---
symbol: "CNTNAP5"
type: "gene"
col: 7864
ensembl_id: "ENSG00000155052"
name: "contactin associated protein family member 5"
location: "2q14.3"
module: 90
arm: "+"
pooled_cpm: 4.6
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 8
tags: ["gene", "module/090"]
generated_by: "tahoemap"
---

# CNTNAP5

*contactin associated protein family member 5* — 2q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.51× (z +21.1, q 0e+00, up in 30 of 34 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USH2A]] (+0.88, fdr 7e-06), [[PTPRT]] (+0.88, fdr 7e-06), [[CNTN5]] (+0.86, fdr 7e-06).
> It is in [[Module 090]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 8 go from it, the strongest it → [[CHRM5]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7864.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.51×** | +21.1 | 0e+00 | 30/34 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.23×** | +16.4 | 0e+00 | 29/34 (C32, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.80×** | +13.2 | 2e-37 | 11/14 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.77×** | +12.6 | 3e-34 | 2/4 (HOP62, A498) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.73×** | +12.0 | 3e-31 | 5/7 (HOP62, A498, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.30×** | +8.2 | 2e-14 | 22/41 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.85×** | +6.1 | 1e-07 | 13/28 (LoVo, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.82×** | +5.9 | 2e-07 | 2/12 (PANC-1, NCI-H1573) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.53×** | +5.9 | 2e-07 | 17/45 (A498, SW480, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +5.8 | 3e-07 | 7/23 (NCI-H460, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.74×** | +5.4 | 3e-06 | 12/33 (C32, HS-578T, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.80×** | +5.3 | 5e-06 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +4.9 | 4e-05 | 10/34 (C32, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +4.8 | 6e-05 | 2/12 (HOP62, A498) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +4.0 | 0.002 | 5/45 (A498, HOP62, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.47×** | +3.8 | 0.005 | 3/44 (A498, SW480, …) | inconsistent across doses | position effect removed |
| [[Bimatoprost (drug)]] 0.5 µM |  | **1.43×** | +3.6 | 0.012 | 4/36 (CFPAC-1, HOP62, …) | inconsistent across doses | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.42×** | +3.5 | 0.016 | 9/40 (C32, SK-MEL-2, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.41×** | +3.3 | 0.032 | 2/36 (A-427, NCI-H1573) | rises with dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +3.1 | 0.045 | 7/29 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.37×** | +3.1 | 0.050 | 3/38 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.53×** | +3.0 | 0.062 | 1/14 (LoVo) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7864.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.901× | -3.6 | 0.16 | 13/47 (NCI-H460, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7864. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 1.81 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.30× (z +9.3) | — |
| [[A498 (line)]] | wt | 2.12 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.03× (z +9.4) | — |
| [[C32 (line)]] | wt | 3.00 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 62.3× (z +14.3) | — |
| [[HEC-1-A (line)]] | alt | 2.47 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.43× (z +9.0) | — |
| [[HS-578T (line)]] | alt | 3.78 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.46× (z +9.0) | — |
| [[LoVo (line)]] | wt | 2.09 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.02× (z +8.8) | — |
| [[NCI-H1573 (line)]] | alt | 2.95 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.63× (z +9.1) | — |
| [[SW480 (line)]] | alt | 2.38 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.47× (z +10.2) | — |
| [[A-172 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.53 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.37 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7864), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USH2A]] | +0.88 | +0.79 / +0.88 | both halves | 7e-06 | **novel candidate** |
| [[PTPRT]] | +0.88 | +0.75 / +0.89 | both halves | 7e-06 | **novel candidate** |
| [[CNTN5]] | +0.86 | +0.76 / +0.84 | both halves | 7e-06 | STRING 573 |
| [[LINC00861]] | +0.85 | +0.76 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[SCHLAP1]] | +0.85 | +0.78 / +0.87 | both halves | 7e-06 | **novel candidate** |
| [[SPATA21]] | +0.84 | +0.79 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[CNBD1]] | +0.84 | +0.78 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[TTN]] | +0.84 | +0.80 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[PPP1R9A-AS1]] | +0.83 | +0.79 / +0.78 | both halves | 7e-06 |  |
| [[CHMP3-AS1]] | +0.83 | +0.71 / +0.77 | both halves | 7e-06 |  |
| [[LRRC4C]] | +0.82 | +0.74 / +0.80 | both halves | 7e-06 |  |
| [[MIR4300HG]] | +0.81 | +0.78 / +0.79 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CNTNAP5's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHRM5]] | C | CNTNAP5's natural level weakens CHRM5's drug response | CNTNAP5's natural level across 44 lines (lineage-adjusted; a glimpse) | r -0.84, reverse -0.36; direction clear | 1e-04 | ⚠ tissue can mimic it; precision caveat |
| [[CLVS1]] | C | CNTNAP5's natural level weakens CLVS1's drug response | CNTNAP5's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.83, reverse -0.30; direction clear | 1e-04 | ⚠ tissue can mimic it; precision caveat |
| [[C2CD5-AS1]] | C | CNTNAP5's natural level weakens C2CD5-AS1's drug response | CNTNAP5's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.67, reverse +0.04; direction clear | 0.026 | ⚠ tissue can mimic it; precision caveat |
| [[UNC79]] | C | CNTNAP5's natural level weakens UNC79's drug response | CNTNAP5's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.66, reverse -0.10; direction clear | 0.043 | ⚠ tissue can mimic it; precision caveat |
| [[PTPRT]] | C | CNTNAP5's natural level weakens PTPRT's drug response | CNTNAP5's natural level across 44 lines (lineage-adjusted; a glimpse) | r -0.67, reverse -0.31; direction clear | 0.063 | ⚠ tissue can mimic it; precision caveat |
| [[LINC02307]] | C | CNTNAP5's natural level weakens LINC02307's drug response | CNTNAP5's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.65, reverse -0.36; direction clear | 0.075 | ⚠ tissue can mimic it; precision caveat |
| [[KCNH1]] | C | CNTNAP5's natural level weakens KCNH1's drug response | CNTNAP5's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.65, reverse -0.49; direction not clear | 0.075 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[MYT1L]] | C | CNTNAP5's natural level weakens MYT1L's drug response | CNTNAP5's natural level across 36 lines (lineage-adjusted; a glimpse) | r -0.72, reverse -0.50; direction not clear | 0.098 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 090]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.883). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (20.8, 29.1); signed map (33.1, 14.6). **Vector** length 48.1, 5.92% of its response variance represented; |z| ≥ 3 in 894 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.3 | +21.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.3 | +16.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.0 | +13.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.6 | +12.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +3.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +0.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.0 | +3.3 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.9 | -3.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -2.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.5 | -0.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -0.5 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.2 | -1.9 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.2 | -1.0 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.2 | -1.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | contactin associated protein family member 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.3 — chr2:124,025,287-124,921,219 (+) |
| Ensembl biotype | protein_coding |
| Also known as | caspr5, FLJ31966 |
| Gene groups (HGNC) | Contactin associated protein family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WYK1](https://www.uniprot.org/uniprotkb/Q8WYK1) (Contactin-associated protein-like 5):

> May play a role in the correct development and proper functioning of the peripheral and central nervous system and be involved in cell adhesion and intercellular communication.

**Summary**, from NCBI Gene [129684](https://www.ncbi.nlm.nih.gov/gene/129684):

> This gene product belongs to the neurexin family, members of which function in the vertebrate nervous system as cell adhesion molecules and receptors. This protein, like other neurexin proteins, contains epidermal growth factor repeats and laminin G domains. In addition, it includes an F5/8 type C domain, discoidin/neuropilin- and fibrinogen-like domains, and thrombospondin N-terminal-like domains. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:18748](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18748) · Entrez [129684](https://www.ncbi.nlm.nih.gov/gene/129684) · UniProt [Q8WYK1](https://www.uniprot.org/uniprotkb/Q8WYK1) · Ensembl [ENSG00000155052](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155052)

## Data

Gene col 7864: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7864); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7864, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7864]; `tensor/DDL_lfc|DDL_z.npy` [7864]; `embed/gene_vectors.npy` [7864]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7864 or target_col == 7864). Every well: [[CNTNAP5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNTNAP5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
