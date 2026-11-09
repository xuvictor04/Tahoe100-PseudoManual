---
symbol: "SLC47A1"
type: "gene"
col: 6625
ensembl_id: "ENSG00000142494"
name: "solute carrier family 47 member 1"
location: "17p11.2"
module: 102
arm: "+"
pooled_cpm: 5.44
n_lines_expressing: 30
n_dd_up: 24
n_dd_down: 1
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 3
tags: ["gene", "module/102"]
generated_by: "tahoemap"
---

# SLC47A1

*solute carrier family 47 member 1* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.76× (z +17.4, q 0e+00, up in 8 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.717× (z -4.0, q 0.035, down in 10 of 20 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SNU-1 0.258×, HepG2/C3A 0.266×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SNU-1 0.148×); [[Rifaximin (drug)]] 5 µM in 1 line (J82 0.0422×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.353×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCD5]] (+0.66, fdr 1e-05), [[LAPTM4B]] (+0.60, fdr 1e-05), [[PARD6G]] (+0.58, fdr 3e-05); moves opposite to [[ZMYM6]] (-0.51, fdr 1e-04), [[DNAL4]] (-0.50, fdr 6e-05), [[DZANK1]] (-0.48, fdr 2e-04).
> It is in [[Module 102]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[PANK1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6625.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.76×** | +17.4 | 0e+00 | 8/22 (A498, A549, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.38×** | +14.7 | 0e+00 | 12/15 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.03×** | +12.9 | 8e-36 | 4/8 (Hs 766T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.59×** | +10.6 | 3e-24 | 6/10 (J82, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.67×** | +6.0 | 3e-07 | 9/19 (A549, A498, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +5.9 | 3e-07 | 8/21 (A498, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +5.6 | 2e-06 | 10/24 (SW480, HOP62, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.57×** | +5.2 | 1e-05 | 8/17 (A549, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +4.7 | 2e-04 | 16/25 (SW480, NCI-H23, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.0 | 0.003 | 2/26 (A498, A549) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.88×** | +4.0 | 0.003 | 1/12 (A549) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +3.8 | 0.006 | 11/26 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.80×** | +3.7 | 0.008 | 5/11 (NCI-H460, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.35×** | +3.7 | 0.009 | 7/27 (PANC-1, NCI-H23, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.35×** | +3.7 | 0.009 | 5/24 (J82, A549, …) | rises with dose |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.47×** | +3.4 | 0.026 | 0/21 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.31×** | +3.3 | 0.028 | 8/22 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.33×** | +3.3 | 0.030 | 6/22 (A549, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Neratinib (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.036 | 0/26 | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.44×** | +3.2 | 0.040 | 3/24 (A549, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.30×** | +3.2 | 0.040 | 2/19 (MIA PaCa-2, C-33 A) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.27×** | +2.9 | 0.088 | 0/25 | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.58×** | +2.9 | 0.092 | 1/23 (MIA PaCa-2) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6625.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SNU-1 0.258×, HepG2/C3A 0.266×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SNU-1 0.148×); [[Rifaximin (drug)]] 5 µM in 1 line (J82 0.0422×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.353×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.717×** | -4.0 | 0.035 | 10/20 (SNU-1, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6625. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 68.6 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.148× (z -12.4) |
| [[A498 (line)]] | wt | 2.64 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.75× (z +9.2) | — |
| [[C32 (line)]] | wt | 2.06 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 59.8× (z +12.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HepG2_C3A (line)]] | wt | 38.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 2.03 | 0 | 1 | — | [[Cinacalcet (drug)]] 0.5 µM 0.0521× (z -8.8) |
| [[Hs 766T (line)]] | wt | 14.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.87× (z +9.1) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 3.74 | 0 | 1 | — | [[Rifaximin (drug)]] 5 µM 0.0422× (z -10.7) |
| [[A-172 (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.991 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.874 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.924 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.950 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.806 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.941 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.828 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.932 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.988 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.24 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6625), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCD5]] | +0.66 | +0.55 / +0.65 | both halves | 1e-05 | **novel candidate** |
| [[LAPTM4B]] | +0.60 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[PARD6G]] | +0.58 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[RBPMS2]] | +0.56 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[SDK2]] | +0.56 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[CACNB4]] | +0.55 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[MED12L]] | +0.55 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[WNK2]] | +0.54 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[MEGF11]] | +0.53 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[ARHGEF26]] | +0.53 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[ADCY1]] | +0.53 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[LONRF2]] | +0.53 | +0.55 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYM6]] | -0.51 | -0.55 / -0.36 | both halves | 1e-04 |  |
| [[DNAL4]] | -0.50 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[DZANK1]] | -0.48 | -0.45 / -0.29 | both halves | 2e-04 |  |
| [[IFT88]] | -0.45 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[SPEF2]] | -0.44 | -0.36 / -0.29 | both halves | 2e-04 |  |
| [[NAGK]] | -0.44 | -0.45 / -0.28 | both halves | 3e-04 |  |
| [[RSPH3]] | -0.44 | -0.37 / -0.36 | both halves | 1e-04 |  |
| [[STK16]] | -0.44 | -0.31 / -0.44 | both halves | 2e-04 |  |
| [[CREB3]] | -0.44 | -0.42 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SLC47A1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PARD6G]] | B | PARD6G activity raises SLC47A1's level | lines that do not express PARD6G (10) vs lines expressing it (40) | 2.43× lower at baseline in the lines without PARD6G | 0.073 | ⚠ within organs, on part of the lines; also absent: CTXN1, NT5M, RRAGD; maybe low, not absent |
| [[LINC02643]] | C | LINC02643 activity raises SLC47A1's level | lines that do not express LINC02643 (38) vs lines expressing it (12) | 4.54× lower at baseline in the lines without LINC02643 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMRN1, GCG, ENSG00000289530; co-absent with the target |
| [[MSI1]] | C | MSI1 activity raises SLC47A1's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 1.73× lower at baseline in the lines without MSI1 | 0.039 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PANK1]] | B | SLC47A1 activity raises PANK1's level | lines that do not express SLC47A1 (20) vs lines expressing it (30) | 1.30× lower at baseline in the lines without SLC47A1 | 0.021 | ⚠ within organs, on part of the lines; also absent: DUSP9, STOX2, NOVA2; maybe low, not absent |
| [[PARD6G]] | B | SLC47A1 activity raises PARD6G's level | lines that do not express SLC47A1 (20) vs lines expressing it (30) | 2.13× lower at baseline in the lines without SLC47A1 | 0.027 | ⚠ within organs, on part of the lines; also absent: DUSP9, STOX2, NOVA2; maybe low, not absent |
| [[GRID1]] | C | SLC47A1 activity raises GRID1's level | lines that do not express SLC47A1 (20) vs lines expressing it (30) | 2.64× lower at baseline in the lines without SLC47A1 | 0.048 | ⚠ within organs, on part of the lines; also absent: DUSP9, STOX2, NOVA2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 102]] — Neuronal System; 45 genes; every member is in the + arm (projection on the module's main direction 0.615). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (3.7, 37.3); signed map (10.8, 0.2). **Vector** length 43.6, 7.72% of its response variance represented; |z| ≥ 3 in 592 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +12.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +14.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +10.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +4.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +17.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +5.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.4 | +3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.4 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +4.0 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -2.0 | -3.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.2 | -2.0 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | -0.1 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.8 | -1.8 |
|  | [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.8 | -1.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -1.4 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | -0.7 | -2.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.7 | -2.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -0.7 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 47 member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p11.2 — chr17:19,495,385-19,579,034 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10847, MATE1 |
| Gene groups (HGNC) | Small nucleolar RNA protein coding host genes; Solute carrier family 47 |
| Reactome | 3 pathways, smallest: SLC-mediated transport of organic cations; SLC-mediated transmembrane transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96FL8](https://www.uniprot.org/uniprotkb/Q96FL8) (Multidrug and toxin extrusion protein 1):

> Multidrug efflux pump that functions as a H(+)/organic cation antiporter. Plays a physiological role in the excretion of cationic compounds including endogenous metabolites, drugs, toxins through the kidney and liver, into urine and bile respectively. Mediates the efflux of endogenous compounds such as creatinine, vitamin B1/thiamine, agmatine and estrone-3-sulfate. May also contribute to regulate the transport of cationic compounds in testis across the blood-testis-barrier (Probable).

**Summary**, from NCBI Gene [55244](https://www.ncbi.nlm.nih.gov/gene/55244):

> This gene is located within the Smith-Magenis syndrome region on chromosome 17. It encodes a protein of unknown function. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:25588](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25588) · Entrez [55244](https://www.ncbi.nlm.nih.gov/gene/55244) · UniProt [Q96FL8](https://www.uniprot.org/uniprotkb/Q96FL8) · Ensembl [ENSG00000142494](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142494)

## Data

Gene col 6625: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6625); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6625, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6625]; `tensor/DDL_lfc|DDL_z.npy` [6625]; `embed/gene_vectors.npy` [6625]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6625 or target_col == 6625). Every well: [[SLC47A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC47A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
