---
symbol: "DNAJC3-DT"
type: "gene"
col: 14495
ensembl_id: "ENSG00000247400"
name: "DNAJC3 divergent transcript"
location: "13q32.1"
module: 21
arm: "+"
pooled_cpm: 7.9
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 0
n_dd_up_clean: 24
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# DNAJC3-DT

*DNAJC3 divergent transcript* — 13q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 10.9× (z +37.9, q 0e+00, up in 40 of 40 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1573 0.258×; ⚠ toxic; transcription drop); [[Roxadustat (drug)]] 5 µM in 1 line (HS-578T 0.0631×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (HT-29 0.237×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BET1]] (+0.70, fdr 1e-05), [[ERO1B]] (+0.69, fdr 7e-06), [[CCNO-DT]] (+0.68, fdr 1e-05); moves opposite to [[IPO9]] (-0.62, fdr 3e-05), [[EIF2B3]] (-0.58, fdr 1e-04), [[AGK]] (-0.57, fdr 3e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14495.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **10.9×** | +37.9 | 0e+00 | 40/40 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.14×** | +12.3 | 2e-32 | 27/35 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.78×** | +11.5 | 3e-28 | 35/45 (HT-29, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.54×** | +10.5 | 2e-23 | 36/46 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.62×** | +10.4 | 3e-23 | 33/39 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.23×** | +9.0 | 2e-17 | 32/47 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.67×** | +8.1 | 3e-14 | 26/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.06×** | +8.1 | 5e-14 | 32/47 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.10×** | +8.0 | 7e-14 | 3/13 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +6.4 | 9e-09 | 19/39 (A498, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **1.72×** | +6.1 | 7e-08 | 23/45 (HT-29, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.71×** | +6.0 | 9e-08 | 20/47 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.77×** | +5.9 | 1e-07 | 10/20 (LoVo, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.45×** | +5.9 | 1e-07 | 19/47 (HOP62, A-172, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +5.5 | 1e-06 | 21/46 (A-172, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.59×** | +5.0 | 2e-05 | 18/45 (SW1417, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.52×** | +4.7 | 9e-05 | 13/45 (J82, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~4% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14495.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1573 0.258×; ⚠ toxic; transcription drop); [[Roxadustat (drug)]] 5 µM in 1 line (HS-578T 0.0631×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (HT-29 0.237×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.800× | -3.6 | 0.16 | 14/47 (HT-29, SNU-1, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.738× | -3.4 | 0.16 | 16/47 (COLO 205, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14495. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 31.5 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.04× (z +13.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.237× (z -8.5) |
| [[SW480 (line)]] | alt | 12.4 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.87× (z +19.5) | — |
| [[A498 (line)]] | wt | 4.64 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.1× (z +15.2) | — |
| [[HOP62 (line)]] | alt | 4.05 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.1× (z +15.2) | — |
| [[HS-578T (line)]] | alt | 3.91 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.0× (z +11.9) | [[Roxadustat (drug)]] 5 µM 0.0631× (z -8.7) |
| [[A-172 (line)]] | wt | 4.12 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 26.9× (z +15.5) | — |
| [[A549 (line)]] | wt | 2.59 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.2× (z +12.7) | — |
| [[AsPC-1 (line)]] | alt | 4.05 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.5× (z +11.3) | — |
| [[BT-474 (line)]] | alt | 5.81 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.8× (z +13.2) | — |
| [[C32 (line)]] | wt | 3.05 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.8× (z +10.1) | — |
| [[CFPAC-1 (line)]] | alt | 3.90 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.7× (z +12.9) | — |
| [[COLO 205 (line)]] | alt | 34.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.58× (z +9.6) | — |
| [[HCT15 (line)]] | alt | 6.46 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.5× (z +11.1) | — |
| [[HEC-1-A (line)]] | alt | 9.33 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.8× (z +17.0) | — |
| [[HepG2_C3A (line)]] | wt | 4.38 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.1× (z +9.0) | — |
| [[Hs 766T (line)]] | wt | 6.80 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.9× (z +13.9) | — |
| [[hTERT-HPNE (line)]] | wt | 2.42 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 34.5× (z +10.8) | — |
| [[J82 (line)]] | alt | 12.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.61× (z +15.8) | — |
| [[KATO III (line)]] | alt | 30.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.01× (z +16.3) | — |
| [[LoVo (line)]] | wt | 6.59 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.9× (z +16.4) | — |
| [[LOX-IMVI (line)]] | wt | 3.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.4× (z +12.4) | — |
| [[LS 180 (line)]] | wt | 7.35 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.57× (z +12.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 3.34 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.5× (z +13.3) | — |
| [[NCI-H1573 (line)]] | alt | 36.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.258× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 4.12 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.17× (z +9.3) | — |
| [[NCI-H2347 (line)]] | alt | 2.64 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.2× (z +11.8) | — |
| [[NCI-H460 (line)]] | wt | 4.08 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.95× (z +14.4) | — |
| [[Panc 03.27 (line)]] | alt | 7.87 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.6× (z +15.9) | — |
| [[PANC-1 (line)]] | alt | 3.01 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.0× (z +17.5) | — |
| [[RKO (line)]] | wt | 7.26 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.1× (z +12.9) | — |
| [[RPMI-7951 (line)]] | alt | 7.22 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.8× (z +11.2) | — |
| [[SHP-77 (line)]] | alt | 15.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.78× (z +9.0) | — |
| [[SNU-423 (line)]] | alt | 4.44 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.6× (z +11.8) | — |
| [[SW 900 (line)]] | alt | 6.99 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.1× (z +11.8) | — |
| [[SW1417 (line)]] | alt | 6.58 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.6× (z +13.7) | — |
| [[A-427 (line)]] | wt | 4.64 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.28 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.21 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14495), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BET1]] | +0.70 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[ERO1B]] | +0.69 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[CCNO-DT]] | +0.68 | +0.64 / +0.56 | both halves | 1e-05 | same gene group |
| [[STX17-DT]] | +0.68 | +0.66 / +0.57 | both halves | 8e-06 |  |
| [[SLC3A1]] | +0.68 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[STX5-DT]] | +0.66 | +0.54 / +0.70 | both halves | 1e-05 | same gene group |
| [[LANCL1-AS1]] | +0.66 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[CHMP3-AS1]] | +0.66 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[HRG-AS1]] | +0.65 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[UPK2]] | +0.65 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[PSMD7-DT]] | +0.64 | +0.65 / +0.59 | both halves | 7e-06 | same gene group |
| [[C1orf56]] | +0.64 | +0.58 / +0.61 | both halves | 8e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IPO9]] | -0.62 | -0.43 / -0.64 | both halves | 3e-05 |  |
| [[EIF2B3]] | -0.58 | -0.34 / -0.42 | both halves | 1e-04 |  |
| [[AGK]] | -0.57 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[GFM1]] | -0.56 | -0.28 / -0.59 | both halves | 3e-04 |  |
| [[FARSB]] | -0.56 | -0.27 / -0.58 | both halves | 3e-04 |  |
| [[NUP93]] | -0.55 | -0.43 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DNAJC3-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.635). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.0, 25.4); signed map (33.1, 0.8). **Vector** length 70.5, 12.0% of its response variance represented; |z| ≥ 3 in 1,036 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.7 | +37.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.6 | +11.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.2 | +8.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +12.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +10.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +5.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.9 | +4.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.8 | +2.4 |
|  | [[Terfenadine (drug)]] 5 µM |  | +1.6 | +1.7 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -2.4 | +10.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | -2.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.3 | +9.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.2 | +8.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | +0.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.7 | -2.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.7 | -3.6 |
|  | [[EX229 (drug)]] 5 µM |  | -1.5 | -1.0 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.2 | -1.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | DNAJC3 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 13q32.1 — chr13:95,648,711-95,676,973 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously DNAJC3-AS1 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:39808](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:39808) · Entrez [100289274](https://www.ncbi.nlm.nih.gov/gene/100289274) · Ensembl [ENSG00000247400](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000247400)

## Data

Gene col 14495: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14495); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14495, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14495]; `tensor/DDL_lfc|DDL_z.npy` [14495]; `embed/gene_vectors.npy` [14495]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14495 or target_col == 14495). Every well: [[DNAJC3-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAJC3-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
