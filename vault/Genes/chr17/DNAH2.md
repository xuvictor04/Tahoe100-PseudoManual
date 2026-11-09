---
symbol: "DNAH2"
type: "gene"
col: 11472
ensembl_id: "ENSG00000183914"
name: "dynein axonemal heavy chain 2"
location: "17p13.1"
module: 90
arm: "+"
pooled_cpm: 3.9
n_lines_expressing: 40
n_dd_up: 24
n_dd_down: 1
n_dd_up_clean: 19
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/090"]
generated_by: "tahoemap"
---

# DNAH2

*dynein axonemal heavy chain 2* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.14× (z +24.5, q 0e+00, up in 19 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.673× (z -4.2, q 0.014, down in 11 of 36 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (HS-578T 0.0547×, SHP-77 0.279×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SHP-77 0.0784×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.178×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.5 µM in 1 line (LS 180 0.0419×); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (HS-578T 0.0896×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H23 0.0469×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PECAM1]] (+0.69, fdr 7e-06), [[LINC01811]] (+0.67, fdr 7e-06), [[GALNT8]] (+0.66, fdr 9e-06).
> It is in [[Module 090]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ATP6V0A4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11472.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.14×** | +24.5 | 0e+00 | 19/25 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.17×** | +17.3 | 0e+00 | 15/26 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.36×** | +12.3 | 1e-32 | 1/5 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.17×** | +11.6 | 5e-29 | 8/35 (A-172, A549, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **2.17×** | +11.6 | 5e-29 | 17/35 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.96×** | +11.5 | 1e-28 | 22/36 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.62×** | +10.2 | 2e-22 | 16/31 (SW480, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.13×** | +8.0 | 9e-14 | 18/33 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.09×** | +7.8 | 5e-13 | 15/31 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.93×** | +6.9 | 2e-10 | 10/34 (A549, SW480, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.92×** | +6.9 | 3e-10 | 2/9 (NCI-H2347, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.80×** | +6.2 | 3e-08 | 8/25 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.87×** | +6.1 | 4e-08 | 1/5 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.75×** | +5.9 | 1e-07 | 11/33 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +5.3 | 5e-06 | 7/25 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +5.2 | 7e-06 | 4/20 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.63×** | +5.2 | 9e-06 | 11/36 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.38×** | +3.4 | 0.021 | 3/31 (A-427, Panc 03.27, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11472.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (HS-578T 0.0547×, SHP-77 0.279×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SHP-77 0.0784×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.178×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.5 µM in 1 line (LS 180 0.0419×); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (HS-578T 0.0896×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H23 0.0469×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.673×** | -4.2 | 0.014 | 11/36 (NCI-H23, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.744× | -3.2 | 0.37 | 12/33 (LS 180, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.748× | -3.1 | 0.37 | 9/35 (SW480, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11472. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 47.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0784× (z -17.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 6.81 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0547× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change · without an alert: [[Hydroxyurea (drug)]] 0.05 µM 0.0896× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 1.15 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.0× (z +10.0) | — |
| [[SW480 (line)]] | alt | 3.32 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.56× (z +8.6) | — |
| [[A-172 (line)]] | wt | 4.35 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.42× (z +9.3) | — |
| [[A549 (line)]] | wt | 1.08 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 29.7× (z +10.0) | — |
| [[C32 (line)]] | wt | 1.68 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.7× (z +9.5) | — |
| [[HEC-1-A (line)]] | alt | 2.09 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.6× (z +9.7) | — |
| [[LoVo (line)]] | wt | 4.00 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.25× (z +9.7) | — |
| [[LS 180 (line)]] | wt | 4.39 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0419× (z -9.9) |
| [[NCI-H23 (line)]] | alt | 3.46 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0469× (z -8.8) |
| [[A-427 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.916 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.766 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.854 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.711 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.958 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.847 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.820 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.813 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.810 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.929 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.37 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11472), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PECAM1]] | +0.69 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[LINC01811]] | +0.67 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[GALNT8]] | +0.66 | +0.70 / +0.57 | both halves | 9e-06 |  |
| [[CACNA1E]] | +0.66 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[SEC1P]] | +0.63 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[PLB1]] | +0.63 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[CATSPERD]] | +0.63 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[ELAPOR1]] | +0.62 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[DLGAP2]] | +0.62 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[PTPRT]] | +0.62 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[LINC01500]] | +0.62 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[C2CD6]] | +0.62 | +0.53 / +0.67 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DNAH2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ADAM28]] | B | ADAM28 activity raises DNAH2's level | lines that do not express ADAM28 (31) vs lines expressing it (19) | 1.82× lower at baseline in the lines without ADAM28 | 0.048 | ⚠ within organs, on part of the lines; also absent: DHRS9, BATF, IGFBP5 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATP6V0A4]] | B | DNAH2 activity raises ATP6V0A4's level | lines that do not express DNAH2 (10) vs lines expressing it (40) | 1.38× lower at baseline in the lines without DNAH2 | 0.099 | ⚠ within organs, on part of the lines; also absent: SLC4A8, NOTCH3, NFATC4; maybe low, not absent |

## Where it sits

- **Module**: [[Module 090]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.670). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.2, 31.9); signed map (31.3, 17.9). **Vector** length 49.3, 7.15% of its response variance represented; |z| ≥ 3 in 934 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.9 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.3 | +6.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +24.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.9 | +6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +11.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.2 | +10.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +11.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +1.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.7 | +0.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.6 | -3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | +0.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.8 | -4.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -1.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -1.2 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.5 | -2.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.4 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | dynein axonemal heavy chain 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:7,717,744-7,833,742 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1503, FLJ46675; previously DNHD3 |
| Gene groups (HGNC) | Dyneins, axonemal inner arm I1/f complex subunits; Dynein heavy chains |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P225](https://www.uniprot.org/uniprotkb/Q9P225) (Dynein axonemal heavy chain 2):

> As part of the axonemal inner dynein arm complex plays a central role in ciliary beat. Expressed in sperm flagellum, it is required for sperm motility. Dyneins are microtubule-based molecular motors possessing ATPase activities that can convert the chemical energy of ATP into relative sliding between adjacent microtubule doublets to generate ciliary bending.

**Summary**, from NCBI Gene [146754](https://www.ncbi.nlm.nih.gov/gene/146754):

> Dyneins are microtubule-associated motor protein complexes composed of several heavy, light, and intermediate chains. The axonemal dyneins, found in cilia and flagella, are components of the outer and inner dynein arms attached to the peripheral microtubule doublets. DNAH2 is an axonemal inner arm dynein heavy chain (Chapelin et al., 1997 [PubMed 9256245]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:2948](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2948) · Entrez [146754](https://www.ncbi.nlm.nih.gov/gene/146754) · UniProt [Q9P225](https://www.uniprot.org/uniprotkb/Q9P225) · Ensembl [ENSG00000183914](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183914)

## Data

Gene col 11472: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11472); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11472, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11472]; `tensor/DDL_lfc|DDL_z.npy` [11472]; `embed/gene_vectors.npy` [11472]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11472 or target_col == 11472). Every well: [[DNAH2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAH2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
