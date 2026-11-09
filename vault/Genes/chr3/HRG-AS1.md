---
symbol: "HRG-AS1"
type: "gene"
col: 12340
ensembl_id: "ENSG00000197099"
name: "HRG and FETUB antisense RNA 1"
location: "3q27.3"
module: 21
arm: "+"
pooled_cpm: 2.54
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# HRG-AS1

*HRG and FETUB antisense RNA 1* — 3q27.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 7.49× (z +25.8, q 0e+00, up in 32 of 33 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Saquinavir (drug)]] 0.5 µM in 1 line (PANC-1 0.0797×); [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM in 1 line (SW480 0.0764×); [[Benztropine (mesylate) (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0581×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LANCL1-AS1]] (+0.85, fdr 7e-06), [[CHMP3-AS1]] (+0.85, fdr 7e-06), [[C2CD5-AS1]] (+0.83, fdr 7e-06).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12340.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.49×** | +25.8 | 0e+00 | 32/33 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.85×** | +13.7 | 2e-40 | 3/3 (A498, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.07×** | +12.7 | 1e-34 | 13/14 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.37×** | +10.2 | 4e-22 | 4/5 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.80×** | +7.5 | 7e-12 | 14/44 (PANC-1, HEC-1-A, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **2.18×** | +7.0 | 2e-10 | 23/39 (SW480, HEC-1-A, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.88×** | +5.7 | 9e-07 | 18/41 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +5.3 | 1e-05 | 10/34 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~11% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.48×** | +5.0 | 3e-05 | 11/35 (PANC-1, SW48, …) | top dose only | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +4.9 | 7e-05 | 9/25 (NCI-H460, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.67×** | +4.6 | 2e-04 | 4/15 (SW1417, RKO, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +4.5 | 4e-04 | 6/20 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~15% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +3.9 | 0.004 | 5/28 (MIA PaCa-2, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +3.8 | 0.006 | 5/29 (SW1417, AsPC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +3.7 | 0.008 | 5/17 (NCI-H1573, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.40×** | +3.0 | 0.072 | 3/38 (LS 180, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +3.0 | 0.086 | 5/44 (Hs 766T, SNU-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12340.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Saquinavir (drug)]] 0.5 µM in 1 line (PANC-1 0.0797×); [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM in 1 line (SW480 0.0764×); [[Benztropine (mesylate) (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0581×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.665× | -3.7 | 0.12 | 5/44 (A498, SNU-1, …) | two highest doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.903× | -3.3 | 0.30 | 12/46 (HepG2/C3A, A-427, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12340. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 2.40 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 27.2× (z +10.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.36× (z +10.3) | — |
| [[HEC-1-A (line)]] | alt | 3.99 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.3× (z +12.6) | — |
| [[NCI-H2030 (line)]] | alt | 1.95 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.84× (z +8.7) | [[Benztropine (mesylate) (drug)]] 0.5 µM 0.0581× (z -8.5) |
| [[PANC-1 (line)]] | alt | 1.94 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.4× (z +12.1) | [[Saquinavir (drug)]] 0.5 µM 0.0797× (z -8.9) |
| [[SW480 (line)]] | alt | 2.23 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.79× (z +11.9) | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.0764× (z -8.8) |
| [[A-172 (line)]] | wt | 2.24 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.7× (z +11.0) | — |
| [[BT-474 (line)]] | alt | 2.55 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.6× (z +9.0) | — |
| [[CFPAC-1 (line)]] | alt | 3.84 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.24× (z +8.7) | — |
| [[HOP62 (line)]] | alt | 1.97 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.5× (z +10.3) | — |
| [[HS-578T (line)]] | alt | 2.18 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.7× (z +9.8) | — |
| [[LoVo (line)]] | wt | 3.48 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.82× (z +8.6) | — |
| [[NCI-H2347 (line)]] | alt | 2.56 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.76× (z +10.0) | — |
| [[NCI-H460 (line)]] | wt | 1.91 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.56× (z +10.2) | — |
| [[A-427 (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.95 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.46 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.11 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12340), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LANCL1-AS1]] | +0.85 | +0.69 / +0.82 | both halves | 7e-06 | same gene group |
| [[CHMP3-AS1]] | +0.85 | +0.75 / +0.83 | both halves | 7e-06 | same gene group |
| [[C2CD5-AS1]] | +0.83 | +0.73 / +0.80 | both halves | 7e-06 | same gene group |
| [[A2ML1-AS1]] | +0.83 | +0.72 / +0.80 | both halves | 7e-06 | same gene group |
| [[UBOX5-AS1]] | +0.82 | +0.67 / +0.82 | both halves | 7e-06 | same gene group |
| [[C12orf40]] | +0.82 | +0.64 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[HPSE2]] | +0.81 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[SPATA21]] | +0.81 | +0.71 / +0.81 | both halves | 7e-06 |  |
| [[CTDSPL2-DT]] | +0.80 | +0.70 / +0.79 | both halves | 7e-06 |  |
| [[SLC3A1]] | +0.80 | +0.76 / +0.76 | both halves | 7e-06 |  |
| [[ST7-AS2]] | +0.80 | +0.71 / +0.75 | both halves | 7e-06 | same gene group |
| [[SPATA1]] | +0.79 | +0.67 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HRG-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PPP1R9A-AS1]] | C | PPP1R9A-AS1's natural level weakens HRG-AS1's drug response | PPP1R9A-AS1's natural level across 44 lines (lineage-adjusted; a glimpse) | r -0.70, reverse -0.32; direction not clear | 0.029 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.871). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.4, 27.0); signed map (33.3, 4.8). **Vector** length 45.0, 5.13% of its response variance represented; |z| ≥ 3 in 933 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.3 | +25.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +13.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.6 | +12.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +10.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +7.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +7.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +3.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.7 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.7 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.5 | -3.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -2.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -0.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.1 | -1.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | +0.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -1.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -2.8 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.0 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | HRG and FETUB antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3q27.3 — chr3:186,579,476-186,772,986 (-) |
| Ensembl biotype | lncRNA |
| Also known as | RP11-573D15.8 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55915](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55915) · Entrez [105374258](https://www.ncbi.nlm.nih.gov/gene/105374258) · Ensembl [ENSG00000197099](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197099)

## Data

Gene col 12340: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12340); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12340, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12340]; `tensor/DDL_lfc|DDL_z.npy` [12340]; `embed/gene_vectors.npy` [12340]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12340 or target_col == 12340). Every well: [[HRG-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HRG-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
