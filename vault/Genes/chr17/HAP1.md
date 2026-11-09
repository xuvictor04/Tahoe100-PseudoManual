---
symbol: "HAP1"
type: "gene"
col: 10428
ensembl_id: "ENSG00000173805"
name: "huntingtin associated protein 1"
location: "17q21.2"
module: 93
arm: "+"
pooled_cpm: 7.16
n_lines_expressing: 38
n_dd_up: 26
n_dd_down: 5
n_dd_up_clean: 22
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 9
direction_downstream: 10
tags: ["gene", "module/093"]
generated_by: "tahoemap"
---

# HAP1

*huntingtin associated protein 1* — 17q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 10.7× (z +20.2, q 0e+00, up in 30 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Belumosudil (drug)]] 5 µM: 0.588× (z -4.4, q 0.007, down in 14 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIR9-1HG]] (+0.71, fdr 7e-06), [[TTLL13]] (+0.67, fdr 7e-06), [[SNAI1]] (+0.65, fdr 7e-06); moves opposite to [[TRMT61B]] (-0.57, fdr 1e-05), [[NDUFAF5]] (-0.56, fdr 2e-05), [[QRSL1]] (-0.56, fdr 1e-05).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[MROH3P]] → it (grade B ⚠); 10 go from it, the strongest it → [[LINC02901]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10428.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **10.7×** | +20.2 | 0e+00 | 30/35 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **8.60×** | +18.4 | 0e+00 | 27/33 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **6.21×** | +15.6 | 0e+00 | 27/34 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.46×** | +15.0 | 0e+00 | 26/29 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.97×** | +13.1 | 3e-37 | 30/34 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.47×** | +10.9 | 1e-25 | 23/30 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.58×** | +10.5 | 1e-23 | 17/22 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.97×** | +8.9 | 3e-17 | 15/28 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.75×** | +8.6 | 4e-16 | 24/34 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.87×** | +7.5 | 4e-12 | 16/34 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.38×** | +7.4 | 9e-12 | 24/33 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.00×** | +5.7 | 7e-07 | 12/27 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **1.93×** | +5.6 | 9e-07 | 8/22 (A549, NCI-H2030, …) | two highest doses | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.90×** | +5.4 | 2e-06 | 16/28 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.87×** | +5.3 | 4e-06 | 16/34 (CFPAC-1, SW480, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.79×** | +4.9 | 3e-05 | 19/33 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.77×** | +4.7 | 1e-04 | 17/33 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.44×** | +4.4 | 3e-04 | 14/34 (Panc 03.27, SW480, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **2.62×** | +4.3 | 5e-04 | 9/33 (PANC-1, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10428.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belumosudil (drug)]] 5 µM |  | **0.588×** | -4.4 | 0.007 | 14/31 (A-427, CFPAC-1, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.627×** | -3.7 | 0.060 | 12/34 (HepG2/C3A, LoVo, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.449×** | -3.6 | 0.063 | 14/25 (BT-474, KATO III, …) | top dose only | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Ataluren (drug)]] 0.5 µM |  | **0.678×** | -3.3 | 0.098 | 9/33 (HCT15, A-427, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 5 µM |  | **0.761×** | -3.3 | 0.098 | 11/34 (LoVo, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | 0.502× | -3.1 | 0.19 | 13/32 (BT-474, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.702× | -3.0 | 0.19 | 14/32 (NCI-H23, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.68 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10428. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 5.23 | 9 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.7× (z +14.9) | — |
| [[SW480 (line)]] | alt | 8.12 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 11.7× (z +12.1) | — |
| [[PANC-1 (line)]] | alt | 10.9 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 9.45× (z +13.0) | — |
| [[A-427 (line)]] | wt | 7.91 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 14.9× (z +10.6) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.104× (z -8.9) |
| [[A549 (line)]] | wt | 4.80 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.3× (z +14.2) | — |
| [[HOP62 (line)]] | alt | 2.11 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.0× (z +10.6) | — |
| [[KATO III (line)]] | alt | 14.7 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.0521× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 4.82 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 13.1× (z +9.3) | — |
| [[NCI-H2030 (line)]] | alt | 11.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 15.9× (z +11.0) | — |
| [[A-172 (line)]] | wt | 1.87 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.4× (z +10.4) | — |
| [[BT-474 (line)]] | alt | 21.4 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0743× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 21.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 7.24× (z +9.3) | — |
| [[HEC-1-A (line)]] | alt | 10.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.12× (z +8.5) | — |
| [[NCI-H1573 (line)]] | alt | 17.3 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0837× (z -10.2) ⚠ cell-cycle shift, explains ~42% of this change |
| [[NCI-H2347 (line)]] | alt | 13.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 8.40× (z +9.8) | — |
| [[Panc 03.27 (line)]] | alt | 17.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 10.4× (z +10.2) | — |
| [[A498 (line)]] | wt | 0.855 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.61 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.15 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.615 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.926 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.75 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.696 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.33 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.511 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.924 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.584 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.03 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10428), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIR9-1HG]] | +0.71 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[TTLL13]] | +0.67 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[SNAI1]] | +0.65 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[CCNYL1]] | +0.63 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[FAM222A]] | +0.62 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[PRKCG]] | +0.62 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[CPNE9]] | +0.61 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[LGMN]] | +0.60 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[LSMEM2]] | +0.60 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[SLC9A1]] | +0.60 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[HSPA2]] | +0.60 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[PYGM]] | +0.59 | +0.60 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRMT61B]] | -0.57 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[NDUFAF5]] | -0.56 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[QRSL1]] | -0.56 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[C5orf22]] | -0.51 | -0.50 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MROH3P]] | B | MROH3P activity raises HAP1's level | lines that do not express MROH3P (29) vs lines expressing it (21) | 2.14× lower at baseline in the lines without MROH3P | 0.002 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[LSR]] | B | LSR activity raises HAP1's level | lines that do not express LSR (19) vs lines expressing it (31) | 2.55× lower at baseline in the lines without LSR | 0.009 | ⚠ within organs, on part of the lines; also absent: ENTPD2, EPHA10, OCLN |
| [[KLF5]] | B | KLF5 activity raises HAP1's level | lines that do not express KLF5 (18) vs lines expressing it (32) | 2.36× lower at baseline in the lines without KLF5 | 0.021 | ⚠ within organs, on part of the lines; also absent: LAMA3, IFNLR1, NCMAP; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers HAP1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PTAFR]] | B | PTAFR activity raises HAP1's level | lines that do not express PTAFR (29) vs lines expressing it (21) | 2.47× lower at baseline in the lines without PTAFR | 0.033 | ⚠ within organs, on part of the lines; also absent: TJP3, BSPRY, KDF1; maybe low, not absent |
| [[MOGAT3]] | B | MOGAT3 activity raises HAP1's level | lines that do not express MOGAT3 (30) vs lines expressing it (20) | 1.30× lower at baseline in the lines without MOGAT3 | 0.056 | ⚠ within organs, on part of the lines; also absent: VIL1, LINC02964, LINC01819 |
| [[LONRF3]] | B | LONRF3 activity raises HAP1's level | lines that do not express LONRF3 (10) vs lines expressing it (40) | 2.35× lower at baseline in the lines without LONRF3 | 0.060 | ⚠ within organs, on part of the lines; also absent: AP1G2, TNFRSF10A-DT, C9orf64 |
| [[CEACAM5]] | B | CEACAM5 activity weakens HAP1's drug response | lines that do not express CEACAM5 (27) vs lines expressing it (8) | the lines without CEACAM5 respond 3.72× as strongly (z diff -3.73); strongest at Homoharringtonine 5 µM: 3.21x vs 0.93x (z diff -5.5) | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881; target measured in part of the lines; artifact flags |
| [[SMIM31]] | B | SMIM31 activity weakens HAP1's drug response | lines that do not express SMIM31 (24) vs lines expressing it (11) | the lines without SMIM31 respond 2.04× as strongly (z diff -2.75); strongest at Idarubicin (hydrochloride) 5 µM: 5.64x vs 1.66x (z diff -3.8) | 0.094 | ⚠ within organs, on part of the lines; also absent: CEACAM5, PPP1R1B, ENSG00000267881; target measured in part of the lines; artifact flags |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02901]] | B | HAP1 activity raises LINC02901's level | lines that do not express HAP1 (12) vs lines expressing it (38) | 1.56× lower at baseline in the lines without HAP1 | 0.073 | ⚠ within organs, on part of the lines; also absent: HID1, NRARP, PDE9A |
| [[KPNA7]] | B | HAP1 activity raises KPNA7's level | lines that do not express HAP1 (12) vs lines expressing it (38) | 1.90× lower at baseline in the lines without HAP1 | 0.078 | ⚠ within organs, on part of the lines; also absent: HID1, NRARP, PDE9A |
| [[LSR]] | B | HAP1 activity raises LSR's level | lines that do not express HAP1 (12) vs lines expressing it (38) | 3.04× lower at baseline in the lines without HAP1 | 0.080 | ⚠ within organs, on part of the lines; also absent: HID1, NRARP, PDE9A |
| [[PYGM]] | B | HAP1 activity raises PYGM's level | lines that do not express HAP1 (12) vs lines expressing it (38) | 1.54× lower at baseline in the lines without HAP1 | 0.081 | ⚠ within organs, on part of the lines; also absent: HID1, NRARP, PDE9A |
| [[MFSD2A]] | B | HAP1 activity lowers MFSD2A's level | lines that do not express HAP1 (12) vs lines expressing it (38) | 1.64× higher at baseline in the lines without HAP1 | 0.083 | ⚠ within organs, on part of the lines; also absent: HID1, NRARP, PDE9A |
| [[TUBB3]] | B | HAP1 activity raises TUBB3's level | lines that do not express HAP1 (12) vs lines expressing it (38) | 1.18× lower at baseline in the lines without HAP1 | 0.084 | ⚠ within organs, on part of the lines; also absent: HID1, NRARP, PDE9A |
| [[LSMEM2]] | B | HAP1 activity raises LSMEM2's level | lines that do not express HAP1 (12) vs lines expressing it (38) | 1.53× lower at baseline in the lines without HAP1 | 0.088 | ⚠ within organs, on part of the lines; also absent: HID1, NRARP, PDE9A |
| [[FAM222A]] | B | HAP1 activity raises FAM222A's level | lines that do not express HAP1 (12) vs lines expressing it (38) | 1.59× lower at baseline in the lines without HAP1 | 0.092 | ⚠ within organs, on part of the lines; also absent: HID1, NRARP, PDE9A |
| cells under [[Homoharringtonine (drug)]] 5 µM | B | HAP1 activity raises the cells' numbers under Homoharringtonine 5 µM (protects the cells) | lines that do not express HAP1 (12) vs lines expressing it (36) | the lines without HAP1: 0.46× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: HID1, NRARP, PDE9A |
| [[TLL2]] | B | HAP1 activity strengthens TLL2's drug response | lines that do not express HAP1 (12) vs lines expressing it (34) | the lines without HAP1 respond 0.86× as strongly (z diff +1.06); strongest at Homoharringtonine 5 µM: 3.26x vs 4.51x (z diff +2.4) | 0.096 | ⚠ within organs, on part of the lines; also absent: HID1, NRARP, PDE9A; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.715). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.6, -18.5); signed map (2.0, 18.5). **Vector** length 89.2, 21.1% of its response variance represented; |z| ≥ 3 in 1,072 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.7 | +13.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.5 | +7.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.8 | +2.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.1 | +10.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +15.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.6 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +7.5 |
|  | [[Vilanterol (drug)]] 5 µM |  | +2.1 | +3.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +1.8 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.1 | -3.7 |
|  | [[NG25 (drug)]] 5 µM |  | -3.0 | -3.6 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.7 | -3.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.5 | -2.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.4 | -3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.4 | -1.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.2 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.0 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | huntingtin associated protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2 — chr17:41,717,742-41,734,644 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HLP, hHLP1, HIP5; previously HAP2 |
| Gene groups (HGNC) | Centriolar satellite proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [P54257](https://www.uniprot.org/uniprotkb/P54257) (Huntingtin-associated protein 1):

> Originally identified as neuronal protein that specifically associates with HTT/huntingtin and the binding is enhanced by an expanded polyglutamine repeat within HTT possibly affecting HAP1 interaction properties. Both HTT and HAP1 are involved in intracellular trafficking and HAP1 is proposed to link HTT to motor proteins and/or transport cargos. Seems to play a role in vesicular transport within neurons and axons such as from early endosomes to late endocytic compartments and to promote …

**Summary**, from NCBI Gene [9001](https://www.ncbi.nlm.nih.gov/gene/9001):

> Huntington's disease (HD), a neurodegenerative disorder characterized by loss of striatal neurons, is caused by an expansion of a polyglutamine tract in the HD protein huntingtin. This gene encodes a protein that interacts with huntingtin, with two cytoskeletal proteins (dynactin and pericentriolar autoantigen protein 1), and with a hepatocyte growth factor-regulated tyrosine kinase substrate. The interactions with cytoskeletal proteins and a kinase substrate suggest a role for this protein in …

**Accessions** — [HGNC:4812](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4812) · Entrez [9001](https://www.ncbi.nlm.nih.gov/gene/9001) · UniProt [P54257](https://www.uniprot.org/uniprotkb/P54257) · Ensembl [ENSG00000173805](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173805)

## Data

Gene col 10428: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10428); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10428, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10428]; `tensor/DDL_lfc|DDL_z.npy` [10428]; `embed/gene_vectors.npy` [10428]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10428 or target_col == 10428). Every well: [[HAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
