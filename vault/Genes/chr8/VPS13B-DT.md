---
symbol: "VPS13B-DT"
type: "gene"
col: 14850
ensembl_id: "ENSG00000253948"
name: "VPS13B divergent transcript"
location: "8q22.2"
module: 15
arm: "+"
pooled_cpm: 13.6
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 4
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# VPS13B-DT

*VPS13B divergent transcript* — 8q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.02× (z +18.5, q 0e+00, up in 44 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.585× (z -6.4, q 1e-07, down in 29 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Alpelisib (drug)]] 0.05 µM in 1 line (SNU-1 0.0686×); [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM in 1 line (H4 0.0573×); [[Bortezomib (drug)]] 5 µM in 1 line (HS-578T 0.0973×; ⚠ toxic); [[Pyridoxine (drug)]] 0.5 µM in 1 line (SNU-1 0.107×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GOT1-DT]] (+0.83, fdr 7e-06), [[TSTD3]] (+0.74, fdr 7e-06), [[GPALPP1]] (+0.74, fdr 7e-06); moves opposite to [[DNAJB1]] (-0.60, fdr 1e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[KLRD1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14850.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.02×** | +18.5 | 0e+00 | 44/45 (HS-578T, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.59×** | +10.9 | 6e-25 | 36/42 (SW1417, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.97×** | +8.1 | 2e-13 | 31/47 (RKO, NCI-H23, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.59×** | +7.8 | 8e-13 | 35/48 (A498, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +7.1 | 2e-10 | 25/46 (HS-578T, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.46×** | +6.3 | 3e-08 | 24/48 (PANC-1, HEC-1-A, …) | rises with dose | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.60×** | +5.6 | 2e-06 | 32/48 (LoVo, RKO, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.44×** | +4.3 | 0.001 | 20/47 (HS-578T, LoVo, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +4.3 | 0.001 | 22/47 (RKO, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.42×** | +4.1 | 0.002 | 17/47 (LoVo, HS-578T, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.42×** | +4.0 | 0.004 | 14/47 (LoVo, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.38×** | +3.8 | 0.007 | 12/47 (KATO III, hTERT-HPNE, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.25×** | +3.7 | 0.008 | 18/48 (HS-578T, HOP62, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.36×** | +3.5 | 0.016 | 16/46 (SW480, NCI-H460, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.35×** | +3.5 | 0.016 | 15/47 (NCI-H2030, NCI-H2347, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.24×** | +3.4 | 0.020 | 15/48 (C32, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14850.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Alpelisib (drug)]] 0.05 µM in 1 line (SNU-1 0.0686×); [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM in 1 line (H4 0.0573×); [[Bortezomib (drug)]] 5 µM in 1 line (HS-578T 0.0973×; ⚠ toxic); [[Pyridoxine (drug)]] 0.5 µM in 1 line (SNU-1 0.107×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.585×** | -6.4 | 1e-07 | 29/47 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.682×** | -4.5 | 0.002 | 16/47 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.699×** | -4.2 | 0.004 | 22/47 (SW480, SNU-423, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.718×** | -3.8 | 0.022 | 18/46 (PANC-1, NCI-H1573, …) | top dose only | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | 0.751× | -3.3 | 0.12 | 14/42 (NCI-H1792, BT-474, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.765× | -3.1 | 0.21 | 12/47 (HT-29, hTERT-HPNE, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14850. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 25.7 | 3 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.26× (z +15.7) | [[Bortezomib (drug)]] 5 µM 0.0973× (z -9.4) ⚠ toxic |
| [[A498 (line)]] | wt | 22.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.40× (z +14.6) | — |
| [[BT-474 (line)]] | alt | 11.0 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.10× (z +10.2) | [[Harringtonine (drug)]] 0.05 µM 0.116× (z -8.9) |
| [[RKO (line)]] | wt | 18.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.52× (z +13.8) | — |
| [[SNU-1 (line)]] | wt | 13.7 | 0 | 2 | — | [[Alpelisib (drug)]] 0.05 µM 0.0686× (z -10.2) |
| [[SW1417 (line)]] | alt | 17.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +9.4) | — |
| [[A-172 (line)]] | wt | 12.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +8.8) | — |
| [[A549 (line)]] | wt | 7.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.83× (z +9.7) | — |
| [[AsPC-1 (line)]] | alt | 7.72 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.04× (z +9.3) | — |
| [[H4 (line)]] | wt | 12.7 | 0 | 1 | — | [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM 0.0573× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 17.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +11.3) | — |
| [[HOP62 (line)]] | alt | 15.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.83× (z +10.4) | — |
| [[LOX-IMVI (line)]] | wt | 11.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.11× (z +10.2) | — |
| [[NCI-H2030 (line)]] | alt | 12.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.01× (z +12.4) | — |
| [[Panc 03.27 (line)]] | alt | 14.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.48× (z +9.3) | — |
| [[PANC-1 (line)]] | alt | 14.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.18× (z +14.9) | — |
| [[SHP-77 (line)]] | alt | 19.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.18× (z +11.5) | — |
| [[SW 900 (line)]] | alt | 10.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.75× (z +11.4) | — |
| [[SW480 (line)]] | alt | 16.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +8.9) | — |
| [[A-427 (line)]] | wt | 7.35 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.81 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.94 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14850), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOT1-DT]] | +0.83 | +0.79 / +0.77 | both halves | 7e-06 | same gene group |
| [[TSTD3]] | +0.74 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[GPALPP1]] | +0.74 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[SPESP1]] | +0.73 | +0.67 / +0.57 | both halves | 9e-06 |  |
| [[CAPN10-DT]] | +0.71 | +0.51 / +0.74 | both halves | 1e-05 | same gene group |
| [[ZNF460-AS1]] | +0.71 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[LINC00115]] | +0.71 | +0.49 / +0.72 | both halves | 2e-05 |  |
| [[RNPC3]] | +0.70 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[LINC00938]] | +0.70 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[MAIP1]] | +0.70 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[BCL2L2-PABPN1]] | +0.70 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[SEC24B-AS1]] | +0.70 | +0.60 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJB1]] | -0.60 | -0.63 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLRD1]] | B | KLRD1 activity lowers VPS13B-DT's level | lines that do not express KLRD1 (8) vs lines expressing it (42) | 1.40× higher at baseline in the lines without KLRD1 | 0.014 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LINC01139]] | B | LINC01139 activity raises VPS13B-DT's level | lines that do not express LINC01139 (24) vs lines expressing it (26) | 1.25× lower at baseline in the lines without LINC01139 | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000260289, NTRK3, CTNNA2 |
| [[TOP2A]] | B | TOP2A activity lowers VPS13B-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity lowers VPS13B-DT's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.826). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-7.1, 23.7); signed map (25.6, -13.6). **Vector** length 104, 24.5% of its response variance represented; |z| ≥ 3 in 831 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.6 | +18.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.6 | +8.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.5 | +10.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.3 | +7.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.3 | +5.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +3.7 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +6.3 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -0.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | +0.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.8 | -6.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.6 | -4.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.5 | -4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -0.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.5 | -2.3 |
|  | [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | -2.1 | -1.6 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.9 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | VPS13B divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 8q22.2 — chr8:98,957,568-99,013,743 (-) |
| Ensembl biotype | lncRNA |
| Also known as | OLC8 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:54375](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:54375) · Entrez [105375666](https://www.ncbi.nlm.nih.gov/gene/105375666) · Ensembl [ENSG00000253948](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000253948)

## Data

Gene col 14850: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14850); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14850, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14850]; `tensor/DDL_lfc|DDL_z.npy` [14850]; `embed/gene_vectors.npy` [14850]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14850 or target_col == 14850). Every well: [[VPS13B-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VPS13B-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
