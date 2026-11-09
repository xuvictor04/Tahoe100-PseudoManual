---
symbol: "KCNJ14"
type: "gene"
col: 11274
ensembl_id: "ENSG00000182324"
name: "potassium inwardly rectifying channel subfamily J member 14"
location: "19q13.33"
module: 5
arm: "+"
pooled_cpm: 18.13
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 15
n_dd_up_clean: 12
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# KCNJ14

*potassium inwardly rectifying channel subfamily J member 14* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.91× (z +10.6, q 3e-23, up in 37 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.636× (z -7.4, q 5e-11, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SYCE2]] (+0.71, fdr 7e-06), [[CDR2]] (+0.68, fdr 7e-06), [[CRK]] (+0.68, fdr 7e-06); moves opposite to [[CAT]] (-0.68, fdr 7e-06), [[DLD]] (-0.67, fdr 1e-05), [[FBXO7]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[HCG18]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11274.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +10.6 | 3e-23 | 37/46 (NCI-H1792, HT-29, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.66×** | +8.2 | 5e-14 | 34/47 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.80×** | +6.8 | 2e-09 | 34/44 (HS-578T, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.87×** | +6.8 | 2e-09 | 30/41 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.60×** | +5.4 | 6e-06 | 28/47 (SW 900, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.60×** | +5.4 | 6e-06 | 27/47 (NCI-H2030, NCI-H2347, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.59×** | +5.4 | 6e-06 | 29/46 (SW480, SNU-1, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.58×** | +5.3 | 9e-06 | 30/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.54×** | +5.0 | 4e-05 | 29/47 (SW480, NCI-H460, …) | rises with dose | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +4.2 | 0.002 | 6/48 (LoVo, AsPC-1, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.97×** | +4.1 | 0.002 | 21/45 (MIA PaCa-2, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.41×** | +4.0 | 0.003 | 19/47 (SW480, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.39×** | +3.8 | 0.006 | 23/47 (NCI-H2347, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.40×** | +3.6 | 0.012 | 18/46 (HS-578T, HOP62, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.81×** | +3.6 | 0.012 | 15/45 (NCI-H460, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.73×** | +3.3 | 0.029 | 13/45 (MIA PaCa-2, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.048 | 14/48 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.34×** | +3.2 | 0.048 | 14/46 (NCI-H460, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +3.0 | 0.088 | 16/47 (NCI-H2347, BT-474, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11274.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.636×** | -7.4 | 5e-11 | 35/48 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.698×** | -4.2 | 0.008 | 22/47 (MIA PaCa-2, NCI-H2030, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.689×** | -4.1 | 0.009 | 15/28 (A498, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.789×** | -3.9 | 0.012 | 16/48 (SW480, SHP-77, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.539×** | -3.8 | 0.019 | 13/48 (RKO, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.800×** | -3.7 | 0.021 | 18/48 (A498, RPMI-7951, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.810×** | -3.4 | 0.045 | 13/48 (AsPC-1, MIA PaCa-2, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.732×** | -3.4 | 0.045 | 18/46 (NCI-H2030, MIA PaCa-2, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.751×** | -3.3 | 0.051 | 16/47 (CHP-212, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.743×** | -3.3 | 0.063 | 19/47 (SK-MEL-2, MIA PaCa-2, …) | all doses, flat |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.750×** | -3.2 | 0.080 | 13/45 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.748×** | -3.1 | 0.080 | 10/47 (SW480, MIA PaCa-2, …) | all doses, flat |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.755×** | -3.1 | 0.091 | 14/45 (HepG2/C3A, HT-29, …) | top dose only |  |
| [[Anethole trithione (drug)]] 0.05 µM |  | **0.771×** | -3.0 | 0.094 | 5/48 (LS 180, PANC-1, …) | inconsistent across doses |  |
| [[Ferulic acid (drug)]] 0.5 µM |  | **0.772×** | -3.0 | 0.094 | 12/46 (hTERT-HPNE, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11274. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 18.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.140× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 28.5 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.187× (z -15.6) |
| [[A-172 (line)]] | wt | 6.78 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.237× (z -9.1) |
| [[A-427 (line)]] | wt | 15.3 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.123× (z -11.0) ⚠ cell-cycle shift, explains ~30% of this change |
| [[BT-474 (line)]] | alt | 17.5 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0912× (z -9.0) ⚠ toxic |
| [[HT-29 (line)]] | alt | 32.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +9.4) | — |
| [[hTERT-HPNE (line)]] | wt | 11.6 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.103× (z -8.8) |
| [[J82 (line)]] | alt | 18.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 24.2 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.381× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 6.16 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +9.1) | — |
| [[NCI-H1792 (line)]] | alt | 17.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.38× (z +10.8) | — |
| [[NCI-H460 (line)]] | wt | 15.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.230× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 19.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +8.9) | — |
| [[RKO (line)]] | wt | 18.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -8.6) |
| [[SW 900 (line)]] | alt | 11.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.08× (z +8.7) | — |
| [[A498 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.51 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.24 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.95 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 27.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11274), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYCE2]] | +0.71 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[CDR2]] | +0.68 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[CRK]] | +0.68 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[IDI2-AS1]] | +0.68 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[PPRC1]] | +0.68 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[P2RY11]] | +0.67 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[PPIEL-1]] | +0.67 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[POLR1C]] | +0.66 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[TRMT1]] | +0.65 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[ISG20L2]] | +0.65 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[FBXO10]] | +0.65 | +0.71 / +0.53 | both halves | 1e-05 |  |
| [[MYH3]] | +0.64 | +0.64 / +0.59 | both halves | 7e-06 | pathway: Muscle contraction |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAT]] | -0.68 | -0.72 / -0.58 | both halves | 7e-06 |  |
| [[DLD]] | -0.67 | -0.51 / -0.68 | both halves | 1e-05 |  |
| [[FBXO7]] | -0.65 | -0.66 / -0.71 | both halves | 7e-06 |  |
| [[FAM199X]] | -0.64 | -0.51 / -0.69 | both halves | 1e-05 |  |
| [[MDH1]] | -0.63 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[VAMP7]] | -0.62 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[LANCL1]] | -0.61 | -0.53 / -0.62 | both halves | 1e-05 |  |
| [[TM7SF3]] | -0.61 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[LTA4H]] | -0.61 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[ALAD]] | -0.59 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[AKTIP]] | -0.59 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[MRS2]] | -0.59 | -0.48 / -0.62 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HCG18]] | C | KCNJ14's natural level strengthens HCG18's drug response | KCNJ14's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.61, reverse +0.07; direction not clear | 0.086 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.619). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (4.5, -9.5); signed map (8.2, 12.0). **Vector** length 109, 27.8% of its response variance represented; |z| ≥ 3 in 958 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +10.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.3 | +5.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.0 | +6.8 |
|  | [[EX229 (drug)]] 5 µM |  | +3.6 | +4.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.3 | +6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +3.2 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +2.6 | +2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.5 | +4.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.5 | +3.3 |
| fall | [[Selinexor (drug)]] 5 µM |  | -6.4 | -7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.9 | -3.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.4 | -0.6 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -2.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.0 | -4.1 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -3.4 | -2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.9 | -3.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.8 | -2.8 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.8 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | potassium inwardly rectifying channel subfamily J member 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:48,455,574-48,466,980 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Kir2.4, IRK4 |
| Gene groups (HGNC) | Potassium inwardly rectifying channel subfamily J |
| Reactome | 6 pathways, smallest: Phase 4 - resting membrane potential; Inwardly rectifying K+ channels; Potassium Channels |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UNX9](https://www.uniprot.org/uniprotkb/Q9UNX9) (ATP-sensitive inward rectifier potassium channel 14):

> Inward rectifier potassium channels are characterized by a greater tendency to allow potassium to flow into the cell rather than out of it. Their voltage dependence is regulated by the concentration of extracellular potassium; as external potassium is raised, the voltage range of the channel opening shifts to more positive voltages.

**Summary**, from NCBI Gene [3770](https://www.ncbi.nlm.nih.gov/gene/3770):

> Potassium channels are present in most mammalian cells, where they participate in a wide range of physiologic responses. The protein encoded by this gene is an integral membrane protein and inward-rectifier type potassium channel, and probably has a role in controlling the excitability of motor neurons. [provided by RefSeq, Feb 2013]

**Accessions** — [HGNC:6260](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6260) · Entrez [3770](https://www.ncbi.nlm.nih.gov/gene/3770) · UniProt [Q9UNX9](https://www.uniprot.org/uniprotkb/Q9UNX9) · Ensembl [ENSG00000182324](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182324)

## Data

Gene col 11274: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11274); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11274, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11274]; `tensor/DDL_lfc|DDL_z.npy` [11274]; `embed/gene_vectors.npy` [11274]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11274 or target_col == 11274). Every well: [[KCNJ14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCNJ14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
