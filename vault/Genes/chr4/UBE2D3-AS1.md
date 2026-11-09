---
symbol: "UBE2D3-AS1"
type: "gene"
col: 14465
ensembl_id: "ENSG00000246560"
name: "UBE2D3 antisense RNA 1"
location: "4q24"
module: 83
arm: "+"
pooled_cpm: 5.76
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 1
n_dd_up_clean: 17
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# UBE2D3-AS1

*UBE2D3 antisense RNA 1* — 4q24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.90× (z +19.1, q 0e+00, up in 35 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Panobinostat (drug)]] 0.05 µM: 0.735× (z -3.9, q 0.048, down in 9 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Imiquimod (maleate) (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0689×); [[Docetaxel (Trihydrate) (drug)]] 0.05 µM in 1 line (A-427 0.108×); [[Simotinib (drug)]] 5 µM in 1 line (NCI-H23 0.114×; ⚠ toxic); [[Capmatinib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0657×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MPDU1]] (+0.84, fdr 7e-06), [[C2orf49-DT]] (+0.82, fdr 7e-06), [[CCT6B]] (+0.82, fdr 7e-06); moves opposite to [[MMS19]] (-0.68, fdr 1e-05), [[BRAT1]] (-0.68, fdr 5e-05), [[LPCAT4]] (-0.68, fdr 1e-04).
> It sits in the **+** arm of [[Module 083]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[LPXN]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14465.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.90×** | +19.1 | 0e+00 | 35/40 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.67×** | +17.6 | 0e+00 | 39/40 (CFPAC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.35×** | +15.4 | 0e+00 | 39/44 (HT-29, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.09×** | +13.3 | 6e-38 | 15/17 (NCI-H460, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.31×** | +10.6 | 3e-24 | 26/38 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.18×** | +9.5 | 2e-19 | 31/44 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.57×** | +8.1 | 3e-14 | 21/47 (HOP62, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.82×** | +7.6 | 2e-12 | 19/29 (AsPC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.47×** | +6.9 | 4e-10 | 25/46 (PANC-1, A498, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +6.7 | 1e-09 | 13/32 (NCI-H1573, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +6.5 | 3e-09 | 14/36 (LOX-IMVI, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.70×** | +6.5 | 5e-09 | 3/7 (HOP62, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.51×** | +5.3 | 6e-06 | 12/47 (CFPAC-1, A498, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.48×** | +5.0 | 2e-05 | 10/43 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +4.7 | 9e-05 | 16/41 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.39×** | +4.2 | 0.001 | 7/47 (A-427, PANC-1, …) | rises with dose |  |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.38×** | +4.1 | 0.002 | 9/39 (NCI-H2030, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.37×** | +4.0 | 0.002 | 11/46 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.34×** | +3.7 | 0.007 | 7/47 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14465.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Imiquimod (maleate) (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0689×); [[Docetaxel (Trihydrate) (drug)]] 0.05 µM in 1 line (A-427 0.108×); [[Simotinib (drug)]] 5 µM in 1 line (NCI-H23 0.114×; ⚠ toxic); [[Capmatinib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0657×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **0.735×** | -3.9 | 0.048 | 9/47 (NCI-H1573, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Radotinib (drug)]] 5 µM |  | 0.829× | -3.4 | 0.19 | 10/46 (PANC-1, SW 1271, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.768× | -3.2 | 0.19 | 13/44 (SHP-77, PANC-1, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | 0.780× | -3.2 | 0.19 | 16/47 (NCI-H1573, C32, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[NG25 (drug)]] 5 µM |  | 0.628× | -3.1 | 0.19 | 8/35 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | 0.634× | -3.0 | 0.19 | 3/43 (PANC-1, NCI-H1573, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | 0.788× | -3.0 | 0.19 | 8/44 (A549, J82, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14465. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 9.98 | 0 | 2 (1 ⚠) | — | [[Docetaxel (Trihydrate) (drug)]] 0.05 µM 0.108× (z -10.1) |
| [[CFPAC-1 (line)]] | alt | 6.83 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +9.0) | — |
| [[NCI-H460 (line)]] | wt | 4.12 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +10.8) | — |
| [[HEC-1-A (line)]] | alt | 6.23 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.00× (z +8.6) | — |
| [[HOP62 (line)]] | alt | 5.63 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +8.9) | — |
| [[HT-29 (line)]] | alt | 6.93 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.98× (z +9.5) | — |
| [[LoVo (line)]] | wt | 8.13 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +10.0) | — |
| [[LOX-IMVI (line)]] | wt | 4.56 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 0.5 µM 0.0689× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 4.25 | 0 | 1 | — | [[Capmatinib (drug)]] 0.05 µM 0.0657× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 9.43 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.114× (z -9.5) ⚠ toxic |
| [[A-172 (line)]] | wt | 3.58 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.73 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.33 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.35 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.34 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.33 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.09 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.75 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.83 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14465), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPDU1]] | +0.84 | +0.76 / +0.67 | both halves | 7e-06 |  |
| [[C2orf49-DT]] | +0.82 | +0.79 / +0.63 | both halves | 7e-06 |  |
| [[CCT6B]] | +0.82 | +0.81 / +0.65 | both halves | 7e-06 |  |
| [[LRP2BP]] | +0.82 | +0.77 / +0.62 | both halves | 7e-06 |  |
| [[PARD6G-AS1]] | +0.81 | +0.75 / +0.67 | both halves | 7e-06 | same gene group |
| [[SMIM15-AS1]] | +0.80 | +0.78 / +0.56 | both halves | 1e-05 | same gene group |
| [[ZNF546]] | +0.79 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[LINC00880]] | +0.79 | +0.75 / +0.56 | both halves | 1e-05 |  |
| [[PCBP1-AS1]] | +0.79 | +0.78 / +0.47 | both halves | 2e-05 | same gene group |
| [[TMEM202-AS1]] | +0.78 | +0.79 / +0.49 | both halves | 1e-05 | same gene group |
| [[GSK3B-DT]] | +0.78 | +0.79 / +0.49 | both halves | 1e-05 |  |
| [[LINC01004]] | +0.77 | +0.69 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMS19]] | -0.68 | -0.70 / -0.54 | both halves | 1e-05 |  |
| [[BRAT1]] | -0.68 | -0.61 / -0.40 | both halves | 5e-05 |  |
| [[LPCAT4]] | -0.68 | -0.70 / -0.34 | both halves | 1e-04 |  |
| [[WRAP73]] | -0.68 | -0.51 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers UBE2D3-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LPXN]] | C | UBE2D3-AS1's natural level strengthens LPXN's drug response | UBE2D3-AS1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse -0.21; direction not clear | 0.079 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **+** arm (projection on the module's main direction 0.776). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (11.0, 11.2); signed map (22.1, -3.8). **Vector** length 80.8, 14.3% of its response variance represented; |z| ≥ 3 in 1,114 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.6 | +15.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.7 | +19.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +17.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +13.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.2 | +6.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +8.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.5 | +4.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.0 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +2.7 |
| fall | [[Belinostat (drug)]] 5 µM |  | -5.2 | -3.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.3 | -3.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | -3.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.8 | -3.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.8 | -3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -2.3 |
|  | [[Brivudine (drug)]] 0.5 µM |  | -1.5 | -1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.2 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | UBE2D3 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 4q24 — chr4:102,827,611-102,844,099 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:54095](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:54095) · Entrez [105377348](https://www.ncbi.nlm.nih.gov/gene/105377348) · Ensembl [ENSG00000246560](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000246560)

## Data

Gene col 14465: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14465); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14465, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14465]; `tensor/DDL_lfc|DDL_z.npy` [14465]; `embed/gene_vectors.npy` [14465]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14465 or target_col == 14465). Every well: [[UBE2D3-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE2D3-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
