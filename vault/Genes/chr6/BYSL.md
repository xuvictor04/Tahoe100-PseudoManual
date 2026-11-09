---
symbol: "BYSL"
type: "gene"
col: 3382
ensembl_id: "ENSG00000112578"
name: "bystin like"
location: "6p21.1"
module: 1
arm: "+"
pooled_cpm: 8.55
n_lines_expressing: 50
n_dd_up: 41
n_dd_down: 0
n_dd_up_clean: 25
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# BYSL

*bystin like* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 41 drug-doses (16 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 11.4× (z +13.8, q 2e-40, up in 46 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.120×, NCI-H23 0.192×); [[Furosemide (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0612×); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H2030 0.157×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Fulvestrant (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.1000×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RRS1]] (+0.86, fdr 7e-06), [[LTV1]] (+0.86, fdr 7e-06), [[GRWD1]] (+0.86, fdr 7e-06).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LTBR]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Belzutifan (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 41 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3382.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **11.4×** | +13.8 | 2e-40 | 46/46 (PANC-1, SW480, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.03×** | +12.0 | 1e-30 | 37/43 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.33×** | +10.7 | 3e-24 | 37/48 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **6.31×** | +10.4 | 3e-23 | 37/43 (SW480, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.64×** | +9.5 | 2e-19 | 38/47 (HT-29, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.37×** | +9.3 | 1e-18 | 36/47 (SW480, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~8% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.29×** | +8.6 | 7e-16 | 34/45 (NCI-H1792, COLO 205, …) | two highest doses | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.06×** | +7.8 | 4e-13 | 31/47 (HS-578T, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.05×** | +7.4 | 8e-12 | 28/38 (A-427, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.59×** | +7.0 | 1e-10 | 26/44 (CFPAC-1, A549, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.86×** | +6.4 | 8e-09 | 26/38 (LOX-IMVI, NCI-H1792, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.77×** | +6.1 | 4e-08 | 24/47 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.73×** | +5.9 | 2e-07 | 26/46 (HOP62, HEC-1-A, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.72×** | +5.8 | 3e-07 | 22/46 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.76×** | +5.7 | 3e-07 | 22/44 (SNU-423, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.37×** | +4.9 | 4e-05 | 19/42 (SK-MEL-2, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.57×** | +4.8 | 4e-05 | 21/47 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[TAK-733 (drug)]] 5 µM |  | **2.35×** | +4.8 | 4e-05 | 19/43 (NCI-H460, A498, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **2.31×** | +4.7 | 6e-05 | 15/41 (SW480, COLO 205, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.51×** | +4.3 | 5e-04 | 17/45 (LoVo, NCI-H1573, …) | top dose only | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.97×** | +3.8 | 0.003 | 10/44 (NCI-H460, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3382.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.120×, NCI-H23 0.192×); [[Furosemide (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0612×); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H2030 0.157×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Fulvestrant (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.1000×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.702× | -3.5 | 0.23 | 8/47 (SW480, HEC-1-A, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 0.742× | -3.2 | 0.36 | 17/46 (A-427, LoVo, …) | rises with dose | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | 0.747× | -3.1 | 0.36 | 13/45 (HepG2/C3A, LOX-IMVI, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3382. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 9.37 | 0 | 1 | — | [[Fulvestrant (drug)]] 0.5 µM 0.1000× (z -8.6) |
| [[HOP62 (line)]] | alt | 5.64 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 7.24× (z +9.2) | — |
| [[NCI-H1792 (line)]] | alt | 5.07 | 0 | 1 | — | [[Furosemide (drug)]] 0.5 µM 0.0612× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 15.3 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.192× (z -9.7) |
| [[PANC-1 (line)]] | alt | 13.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 12.0× (z +9.2) | — |
| [[RKO (line)]] | wt | 17.7 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.120× (z -10.7) |
| [[SNU-1 (line)]] | wt | 13.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0943× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.76 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.05 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.87 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.58 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.72 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.92 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.92 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3382), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRS1]] | +0.86 | +0.86 / +0.82 | both halves | 7e-06 | STRING 945 |
| [[LTV1]] | +0.86 | +0.83 / +0.85 | both halves | 7e-06 | same gene group; pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 999 |
| [[GRWD1]] | +0.86 | +0.86 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 958 |
| [[MAK16]] | +0.84 | +0.84 / +0.85 | both halves | 7e-06 | STRING 938 |
| [[TWNK]] | +0.84 | +0.88 / +0.79 | both halves | 7e-06 |  |
| [[POLR1A]] | +0.84 | +0.86 / +0.82 | both halves | 7e-06 | STRING 856 |
| [[NOP16]] | +0.82 | +0.83 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2 |
| [[ZNF202]] | +0.81 | +0.82 / +0.77 | both halves | 7e-06 |  |
| [[DDX10]] | +0.80 | +0.80 / +0.81 | both halves | 7e-06 | same gene group; STRING 971 |
| [[DDX31]] | +0.80 | +0.79 / +0.79 | both halves | 7e-06 | STRING 732 |
| [[MRTO4]] | +0.80 | +0.83 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 954 |
| [[NOP2]] | +0.79 | +0.80 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 915 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LTBR]] | B | LTBR activity lowers BYSL's level | lines that do not express LTBR (8) vs lines expressing it (42) | 1.36× higher at baseline in the lines without LTBR | 0.060 | ⚠ within organs, on part of the lines; also absent: SIGIRR, YPEL3, CLCF1 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Belzutifan (drug)]] 5 µM | C | BYSL's natural level raises the cells' numbers under Belzutifan 5 µM (protects the cells) | BYSL's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.58 | 0.491 over the table, 0.092 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.853). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-15.9, -37.0); signed map (-1.4, -44.8). **Vector** length 92.2, 20.4% of its response variance represented; |z| ≥ 3 in 1,120 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.62 to 15); *Mitochondrial mRNA modification* (reactome, mean cos +0.53 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.9 | +9.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.1 | +10.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.8 | +7.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.6 | +4.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.6 | +13.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.0 | +5.8 |
|  | [[EX229 (drug)]] 5 µM |  | +3.1 | +4.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.0 | +3.6 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.8 | -1.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.7 | -2.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.2 | -0.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.0 | -1.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | -1.9 | +3.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.7 | -2.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | bystin like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:41,921,499-41,933,046 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Enp1 |
| Gene groups (HGNC) | SSU processome |
| Hallmark sets | MYC_TARGETS_V2 |
| Reactome | 4 pathways, smallest: Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol; rRNA processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13895](https://www.uniprot.org/uniprotkb/Q13895) (Bystin):

> Required for processing of 20S pre-rRNA precursor and biogenesis of 40S ribosomal subunits. May be required for trophinin-dependent regulation of cell adhesion during implantation of human embryos.

**Summary**, from NCBI Gene [705](https://www.ncbi.nlm.nih.gov/gene/705):

> Bystin is expressed as a 2-kb major transcript and a 3.6-kb minor transcript in SNG-M cells and in human trophoblastic teratocarcinoma HT-H cells. Protein binding assays determined that bystin binds directly to trophinin and tastin, and that binding is enhanced when cytokeratins 8 and 18 are present. Immunocytochemistry of HT-H cells showed that bystin colocalizes with trophinin, tastin, and the cytokeratins, suggesting that these molecules form a complex in trophectoderm cells at the time of …

**Accessions** — [HGNC:1157](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1157) · Entrez [705](https://www.ncbi.nlm.nih.gov/gene/705) · UniProt [Q13895](https://www.uniprot.org/uniprotkb/Q13895) · Ensembl [ENSG00000112578](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112578)

## Data

Gene col 3382: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3382); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3382, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3382]; `tensor/DDL_lfc|DDL_z.npy` [3382]; `embed/gene_vectors.npy` [3382]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3382 or target_col == 3382). Every well: [[BYSL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BYSL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
