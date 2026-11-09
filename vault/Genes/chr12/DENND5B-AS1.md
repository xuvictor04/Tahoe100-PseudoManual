---
symbol: "DENND5B-AS1"
type: "gene"
col: 14961
ensembl_id: "ENSG00000255867"
name: "DENND5B antisense RNA 1"
location: "12p11.21"
module: 80
arm: "+"
pooled_cpm: 2.85
n_lines_expressing: 44
n_dd_up: 13
n_dd_down: 4
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 2
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# DENND5B-AS1

*DENND5B antisense RNA 1* — 12p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 16.0× (z +29.6, q 0e+00, up in 25 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.523× (z -4.9, q 6e-04, down in 17 of 37 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 5 µM in 1 line (PANC-1 0.100×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.154×); [[Digitoxin (drug)]] 0.5 µM in 1 line (PANC-1 0.132×; ⚠ cell-cycle shift, explains ~45% of this change).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP1R12A-AS2]] (+0.76, fdr 1e-05), [[SPESP1]] (+0.74, fdr 1e-05), [[ATE1OSP]] (+0.74, fdr 1e-05).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[AMY2B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14961.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **16.0×** | +29.6 | 0e+00 | 25/26 (LoVo, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **7.77×** | +14.9 | 0e+00 | 19/22 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.34×** | +10.7 | 3e-24 | 1/5 (NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.95×** | +10.0 | 3e-21 | 22/26 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.38×** | +9.3 | 3e-18 | 18/38 (HOP62, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.60×** | +7.2 | 5e-11 | 4/9 (SW 900, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.83×** | +6.4 | 9e-09 | 14/31 (HOP62, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.28×** | +5.8 | 6e-07 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.87×** | +4.7 | 1e-04 | 14/35 (AsPC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.48×** | +4.2 | 0.002 | 9/37 (NCI-H460, MIA PaCa-2, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.76×** | +4.1 | 0.002 | 4/11 (MIA PaCa-2, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.69×** | +4.0 | 0.003 | 8/29 (MIA PaCa-2, C32, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.51×** | +3.1 | 0.085 | 5/30 (SHP-77, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14961.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 5 µM in 1 line (PANC-1 0.100×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.154×); [[Digitoxin (drug)]] 0.5 µM in 1 line (PANC-1 0.132×; ⚠ cell-cycle shift, explains ~45% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.523×** | -4.9 | 6e-04 | 17/37 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.532×** | -4.8 | 6e-04 | 15/37 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.540×** | -4.6 | 7e-04 | 17/39 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.565×** | -4.3 | 0.002 | 19/39 (A-427, MIA PaCa-2, …) | rises with dose |  |
| [[Baicalin (drug)]] 5 µM |  | 0.739× | -3.2 | 0.15 | 4/41 (J82, SHP-77, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.662× | -3.1 | 0.17 | 13/35 (PANC-1, SW48, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.665× | -3.1 | 0.17 | 14/34 (MIA PaCa-2, PANC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14961. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 3.60 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.68× (z +12.7) | [[Ixazomib citrate (drug)]] 5 µM 0.100× (z -9.6) |
| [[HOP62 (line)]] | alt | 2.59 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.8× (z +11.6) | — |
| [[SW 900 (line)]] | alt | 4.63 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.2× (z +12.1) | — |
| [[SW480 (line)]] | alt | 1.47 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.2× (z +11.9) | — |
| [[A-427 (line)]] | wt | 13.5 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.154× (z -8.9) |
| [[A498 (line)]] | wt | 1.57 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.2× (z +10.4) | — |
| [[A549 (line)]] | wt | 2.40 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.7× (z +9.9) | — |
| [[HEC-1-A (line)]] | alt | 0.755 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 54.1× (z +11.9) | — |
| [[HT-29 (line)]] | alt | 1.12 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 35.1× (z +10.1) | — |
| [[J82 (line)]] | alt | 1.31 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.4× (z +10.0) | — |
| [[KATO III (line)]] | alt | 1.45 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.3× (z +9.9) | — |
| [[LoVo (line)]] | wt | 1.90 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 36.7× (z +13.6) | — |
| [[LOX-IMVI (line)]] | wt | 2.77 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.0× (z +9.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 9.46 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.3× (z +12.8) | — |
| [[SW1417 (line)]] | alt | 1.52 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.2× (z +9.3) | — |
| [[A-172 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.989 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.491 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.662 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.385 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.915 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.718 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.385 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.774 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.65 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.624 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.897 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.642 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.22 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14961), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R12A-AS2]] | +0.76 | +0.67 / +0.50 | both halves | 1e-05 | same gene group |
| [[SPESP1]] | +0.74 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[ATE1OSP]] | +0.74 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[PBLD]] | +0.73 | +0.68 / +0.26 | both halves | 3e-04 |  |
| [[SPEN-AS1]] | +0.72 | +0.66 / +0.55 | both halves | 1e-05 | same gene group |
| [[EFCAB5]] | +0.72 | +0.64 / +0.41 | both halves | 4e-05 |  |
| [[RASSF8-AS1]] | +0.71 | +0.69 / +0.59 | both halves | 7e-06 | same gene group |
| [[SEPTIN7-DT]] | +0.71 | +0.67 / +0.43 | both halves | 3e-05 |  |
| [[CCDC90B-AS1]] | +0.71 | +0.63 / +0.41 | both halves | 4e-05 | same gene group |
| [[TMEM202-AS1]] | +0.70 | +0.63 / +0.41 | both halves | 4e-05 | same gene group |
| [[ZNF425]] | +0.70 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[ZBED5]] | +0.70 | +0.68 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DENND5B-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MIR1915HG]] | B | MIR1915HG activity raises DENND5B-AS1's level | lines that do not express MIR1915HG (13) vs lines expressing it (37) | 1.63× lower at baseline in the lines without MIR1915HG | 0.024 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, NT5M, SOCS2; maybe low, not absent |
| [[FST]] | B | FST activity lowers DENND5B-AS1's level | lines that do not express FST (26) vs lines expressing it (24) | 1.21× higher at baseline in the lines without FST | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IDO1, FN1, CDH2 |
| [[HDAC6]] | B | HDAC6 activity raises DENND5B-AS1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LINC00944]] | B | LINC00944 activity lowers DENND5B-AS1's level | lines that do not express LINC00944 (20) vs lines expressing it (30) | 1.39× higher at baseline in the lines without LINC00944 | 0.070 | ⚠ within organs, on part of the lines; also absent: RDUR, ENSG00000289600, LINC02405 |
| [[C1QTNF1-AS1]] | B | C1QTNF1-AS1 activity lowers DENND5B-AS1's level | lines that do not express C1QTNF1-AS1 (24) vs lines expressing it (26) | 1.55× higher at baseline in the lines without C1QTNF1-AS1 | 0.078 | ⚠ within organs, on part of the lines; also absent: ADAMTS12, ENSG00000287335, FBLN2; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AMY2B]] | B | DENND5B-AS1 activity lowers AMY2B's level | lines that do not express DENND5B-AS1 (6) vs lines expressing it (44) | 1.81× higher at baseline in the lines without DENND5B-AS1 | 0.043 | ⚠ within organs, on part of the lines; also absent: DBN1, DENND5B; maybe low, not absent |
| [[LINC01762]] | B | DENND5B-AS1 activity lowers LINC01762's level | lines that do not express DENND5B-AS1 (6) vs lines expressing it (44) | 1.58× higher at baseline in the lines without DENND5B-AS1 | 0.069 | ⚠ within organs, on part of the lines; also absent: DBN1, DENND5B; maybe low, not absent |

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction 0.733). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (7.9, 20.2); signed map (26.6, -5.9). **Vector** length 62.3, 11.1% of its response variance represented; |z| ≥ 3 in 1,002 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.7 | +29.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +14.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.0 | +9.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.2 | +6.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +10.0 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.6 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +3.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.3 | +1.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.3 | +1.8 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -4.1 | -4.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -3.9 | -4.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -3.7 | -4.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.2 | -4.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.0 | -0.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.8 | -2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.7 | -0.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.4 | -2.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -2.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | DENND5B antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 12p11.21 — chr12:31,589,923-31,615,666 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:42517](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:42517) · Entrez [100874249](https://www.ncbi.nlm.nih.gov/gene/100874249) · Ensembl [ENSG00000255867](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000255867)

## Data

Gene col 14961: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14961); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14961, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14961]; `tensor/DDL_lfc|DDL_z.npy` [14961]; `embed/gene_vectors.npy` [14961]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14961 or target_col == 14961). Every well: [[DENND5B-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DENND5B-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
