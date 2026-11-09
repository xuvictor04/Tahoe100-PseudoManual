---
symbol: "PITPNM1"
type: "gene"
col: 3156
ensembl_id: "ENSG00000110697"
name: "phosphatidylinositol transfer protein membrane associated 1"
location: "11q13.2"
module: 2
arm: "+"
pooled_cpm: 12.66
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 11
n_dd_up_clean: 5
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# PITPNM1

*phosphatidylinositol transfer protein membrane associated 1* — 11q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Belinostat (drug)]] 0.5 µM: 1.58× (z +5.5, q 2e-05, up in 24 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.658× (z -5.1, q 1e-04, down in 26 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TESK1]] (+0.68, fdr 7e-06), [[MAPK11]] (+0.68, fdr 1e-05), [[EHBP1L1]] (+0.68, fdr 7e-06); moves opposite to [[COA6]] (-0.56, fdr 3e-05), [[YARS2]] (-0.56, fdr 8e-05), [[ACOT2]] (-0.51, fdr 1e-04).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3156.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 0.5 µM |  | **1.58×** | +5.5 | 2e-05 | 24/44 (CFPAC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +5.4 | 2e-05 | 11/22 (NCI-H2030, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.37×** | +3.8 | 0.025 | 18/46 (NCI-H460, H4, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.41×** | +3.7 | 0.025 | 10/29 (SHP-77, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.35×** | +3.6 | 0.037 | 12/41 (PANC-1, C32, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.35×** | +3.5 | 0.037 | 17/47 (PANC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.064 | 15/47 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.064 | 10/44 (H4, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.32×** | +3.3 | 0.065 | 12/33 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3156.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.658×** | -5.1 | 1e-04 | 26/47 (NCI-H1573, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.745×** | -5.1 | 1e-04 | 23/43 (SW 900, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.697×** | -4.4 | 0.002 | 23/47 (NCI-H1573, BT-474, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.692×** | -4.3 | 0.002 | 15/46 (NCI-H23, NCI-H1573, …) | rises with dose | composition shift; position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **0.711×** | -4.1 | 0.004 | 18/45 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.717×** | -4.0 | 0.004 | 20/45 (NCI-H1573, LOX-IMVI, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.710×** | -4.0 | 0.004 | 13/46 (NCI-H2030, Panc 03.27, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.793×** | -4.0 | 0.004 | 22/46 (Hs 766T, KATO III, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.729×** | -3.7 | 0.012 | 15/43 (C-33 A, NCI-H23, …) | top dose only | cell-cycle shift (explains ~6% here); position effect removed |
| [[Allantoin (drug)]] 5 µM |  | **0.808×** | -3.7 | 0.012 | 12/47 (Hs 766T, A-172, …) | rises with dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.730×** | -3.7 | 0.012 | 17/43 (MIA PaCa-2, NCI-H23, …) | top dose only | cell-cycle shift (explains ~2% here); position effect removed |
| [[NG25 (drug)]] 5 µM |  | 0.618× | -3.1 | 0.11 | 11/40 (KATO III, HT-29, …) | top dose only | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3156. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 35.5 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.177× (z -13.1) |
| [[LOX-IMVI (line)]] | wt | 9.71 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.173× (z -8.9) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A-172 (line)]] | wt | 11.4 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.182× (z -9.5) |
| [[A-427 (line)]] | wt | 11.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.103× (z -12.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 7.75 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0570× (z -10.9) |
| [[HCT15 (line)]] | alt | 8.68 | 0 | 1 | — | [[Darinaparsin (drug)]] 0.5 µM 0.0694× (z -9.0) |
| [[Hs 766T (line)]] | wt | 30.8 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.183× (z -13.0) |
| [[HS-578T (line)]] | alt | 14.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.187× (z -8.8) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H2030 (line)]] | alt | 10.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.175× (z -9.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 16.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +10.4) ⚠ cell-cycle shift, explains ~77% of this change | — |
| [[A498 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.65 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.46 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.88 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.74 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.20 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.75 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.89 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.45 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3156), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TESK1]] | +0.68 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[MAPK11]] | +0.68 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[EHBP1L1]] | +0.68 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[PLCB3]] | +0.65 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[SIPA1]] | +0.64 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[PCNX3]] | +0.64 | +0.58 / +0.63 | both halves | 8e-06 |  |
| [[SBF1]] | +0.64 | +0.61 / +0.58 | both halves | 7e-06 | pathway: Phospholipid metabolism |
| [[PPP1R12C]] | +0.63 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[ZNF598]] | +0.63 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[TUBGCP6]] | +0.62 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[R3HDM4]] | +0.62 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[ADCK5]] | +0.61 | +0.47 / +0.51 | both halves | 2e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COA6]] | -0.56 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[YARS2]] | -0.56 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[ACOT2]] | -0.51 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[ZNF148]] | -0.51 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[NDUFC1]] | -0.50 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[MTREX]] | -0.50 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[GTF2IRD2B]] | -0.50 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[ENOSF1]] | -0.50 | -0.51 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PITPNM1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity lowers PITPNM1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TMEM184B]] | C | TMEM184B's natural level strengthens PITPNM1's drug response | TMEM184B's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.61, reverse -0.23; direction not clear | 0.0995 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.732). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (14.3, -3.5); signed map (-10.0, 29.6). **Vector** length 90.1, 18.6% of its response variance represented; |z| ≥ 3 in 857 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +5.5 | +5.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +5.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +4.6 | +3.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +3.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +3.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.3 | +3.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.2 | +2.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.2 | +0.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +2.0 |
|  | [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | +2.0 | +1.8 |
| fall | [[Selinexor (drug)]] 5 µM |  | -3.8 | -4.0 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -3.3 | -4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -2.5 |
|  | [[NG25 (drug)]] 5 µM |  | -2.6 | -3.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -2.3 | -4.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | -4.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.2 | -1.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -1.8 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -2.1 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol transfer protein membrane associated 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.2 — chr11:67,491,768-67,506,263 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DRES9, NIR2, RDGB1, RDGBA1, Rd9, RDGB; previously PITPNM |
| Gene groups (HGNC) | Phosphatidylinositol transfer proteins |
| Reactome | 4 pathways, smallest: Synthesis of PI; Glycerophospholipid biosynthesis; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [O00562](https://www.uniprot.org/uniprotkb/O00562) (Membrane-associated phosphatidylinositol transfer protein 1):

> Membrane-associated phosphatidylinositol (PI) transfer protein that shuttles PI between intracellular membranes and thereby maintains plasma-membrane phosphoinositide signaling competence. Transfers phosphatidylinositol from the endoplasmic reticulum to the plasma membrane and mediates counter-transport of phosphatidic acid (PA) from the plasma membrane to the endoplasmic reticulum at endoplasmic reticulum-plasma membrane contact sites, this PI/PA exchange is required for sustained PLC-coupled …

**Summary**, from NCBI Gene [9600](https://www.ncbi.nlm.nih.gov/gene/9600):

> PITPNM1 belongs to a family of membrane-associated phosphatidylinositol transfer domain-containing proteins that share homology with the Drosophila retinal degeneration B (rdgB) protein (Ocaka et al., 2005 [PubMed 15627748]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:9003](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9003) · Entrez [9600](https://www.ncbi.nlm.nih.gov/gene/9600) · UniProt [O00562](https://www.uniprot.org/uniprotkb/O00562) · Ensembl [ENSG00000110697](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110697)

## Data

Gene col 3156: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3156); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3156, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3156]; `tensor/DDL_lfc|DDL_z.npy` [3156]; `embed/gene_vectors.npy` [3156]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3156 or target_col == 3156). Every well: [[PITPNM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PITPNM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
