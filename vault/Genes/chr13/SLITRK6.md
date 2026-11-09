---
symbol: "SLITRK6"
type: "gene"
col: 11551
ensembl_id: "ENSG00000184564"
name: "SLIT and NTRK like family member 6"
location: "13q31.1"
module: 9
arm: "+"
pooled_cpm: 6.46
n_lines_expressing: 22
n_dd_up: 9
n_dd_down: 24
n_dd_up_clean: 6
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 24
direction_downstream: 14
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# SLITRK6

*SLIT and NTRK like family member 6* — 13q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.90× (z +9.3, q 1e-17, up in 1 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.52× (z +5.4, q 1e-05, up in 7 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.566× (z -7.3, q 2e-10, down in 12 of 16 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MGAT4C]] (+0.65, fdr 1e-05), [[CDH12]] (+0.64, fdr 4e-05), [[GABRA2]] (+0.64, fdr 1e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 24 arrows point to it, the strongest [[LINC02315]] → it (grade B ⚠); 14 go from it, the strongest it → [[NR4A2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11551.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.90×** | +9.3 | 1e-17 | 1/5 (NCI-H1573) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.59×** | +8.6 | 2e-15 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.12×** | +6.3 | 6e-08 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.52×** | +5.4 | 1e-05 | 7/19 (KATO III, BT-474, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.73×** | +3.5 | 0.046 | 1/11 (A-427) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.45×** | +3.4 | 0.060 | 0/17 | inconsistent across doses |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **1.45×** | +3.4 | 0.060 | 2/17 (BT-474, KATO III) | two highest doses |  |
| [[Tofacitinib (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.060 | 3/18 (BT-474, KATO III, …) | rises with dose |  |
| [[Ixazomib (drug)]] 0.05 µM |  | **1.46×** | +3.2 | 0.084 | 1/17 (BT-474) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | 1.62× | +3.1 | 0.10 | 1/15 (SHP-77) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 1.40× | +3.1 | 0.10 | 2/17 (Hs 766T, NCI-H1573) | top dose only |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | 1.40× | +3.0 | 0.10 | 0/11 | inconsistent across doses | low cells (technical?) |
| [[Carbamazepine (drug)]] 5 µM |  | 1.39× | +3.0 | 0.10 | 5/17 (NCI-H1573, hTERT-HPNE, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11551.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.566×** | -7.3 | 2e-10 | 12/16 (NCI-H1573, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.511×** | -6.1 | 4e-07 | 11/17 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.522×** | -5.9 | 8e-07 | 7/17 (SHP-77, CHP-212, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.669×** | -5.1 | 4e-05 | 15/17 (CHP-212, SHP-77, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.576×** | -5.0 | 7e-05 | 8/17 (SHP-77, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.574×** | -4.8 | 1e-04 | 8/17 (NCI-H1573, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.615×** | -4.4 | 9e-04 | 10/16 (LS 180, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.633×** | -4.1 | 0.003 | 8/18 (H4, SHP-77, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.637×** | -4.1 | 0.003 | 9/19 (SHP-77, CHP-212, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.641×** | -4.0 | 0.003 | 12/19 (SHP-77, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.655×** | -3.8 | 0.007 | 7/15 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.756×** | -3.6 | 0.016 | 11/19 (NCI-H1573, HT-29, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.674×** | -3.6 | 0.016 | 7/17 (HT-29, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.684×** | -3.4 | 0.024 | 8/18 (NCI-H23, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.686×** | -3.4 | 0.025 | 10/17 (KATO III, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.687×** | -3.4 | 0.025 | 8/18 (SNU-1, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Asciminib (drug)]] 0.05 µM |  | **0.689×** | -3.4 | 0.026 | 2/17 (RPMI-7951, NCI-H1573) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11551. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 64.9 | 0 | 15 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -18.4) |
| [[CHP-212 (line)]] | wt | 487 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.123× (z -19.3) |
| [[HT-29 (line)]] | alt | 18.1 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0903× (z -15.2) |
| [[NCI-H1573 (line)]] | alt | 39.4 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0252× (z -25.8) |
| [[KATO III (line)]] | alt | 6.61 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0691× (z -10.3) |
| [[SNU-1 (line)]] | wt | 18.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.155× (z -9.7) |
| [[A-427 (line)]] | wt | 14.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.126× (z -9.2) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 7.21 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0310× (z -8.7) ⚠ unreliable plate only |
| [[Hs 766T (line)]] | wt | 5.92 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0353× (z -10.5) ⚠ cell-cycle shift, explains ~50% of this change |
| [[LS 180 (line)]] | wt | 4.10 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0550× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 6.20 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0681× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 0.888 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.870 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.700 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.892 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.843 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.867 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.950 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.941 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.901 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.932 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.916 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.874 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.863 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.865 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.852 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.674 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.905 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.748 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.769 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11551), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MGAT4C]] | +0.65 | +0.53 / +0.61 | both halves | 1e-05 | **novel candidate** |
| [[CDH12]] | +0.64 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[GABRA2]] | +0.64 | +0.55 / +0.59 | both halves | 1e-05 | pathway: Neuronal System |
| [[CDH10]] | +0.62 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[VAV3]] | +0.62 | +0.48 / +0.46 | both halves | 3e-05 | **novel candidate** |
| [[SRRM4]] | +0.62 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[SYT4]] | +0.62 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[FGF14]] | +0.62 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[KHDRBS2]] | +0.61 | +0.39 / +0.58 | both halves | 6e-05 |  |
| [[ESRRG]] | +0.61 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[LINC02197]] | +0.61 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[LINC02484]] | +0.60 | +0.38 / +0.57 | both halves | 6e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 1, C 23. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02315]] | B | LINC02315 activity raises SLITRK6's level | lines that do not express LINC02315 (31) vs lines expressing it (19) | 1.38× lower at baseline in the lines without LINC02315 | 0.067 | ⚠ within organs, on part of the lines; also absent: GABRG2, COX7B2, SLC25A24P1 |
| [[FUT9]] | C | FUT9 activity raises SLITRK6's level | lines that do not express FUT9 (40) vs lines expressing it (10) | 5.88× lower at baseline in the lines without FUT9 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, KCNH7, GCG; co-absent with the target |
| [[GTSF1]] | C | GTSF1 activity raises SLITRK6's level | lines that do not express GTSF1 (40) vs lines expressing it (10) | 3.26× lower at baseline in the lines without GTSF1 | 0.009 | ⚠ within organs, on part of the lines; also absent: CGA, CALCA, LINC02566; co-absent with the target |
| [[C2CD4A]] | C | C2CD4A activity raises SLITRK6's level | lines that do not express C2CD4A (38) vs lines expressing it (12) | 2.81× lower at baseline in the lines without C2CD4A | 0.010 | ⚠ within organs, on part of the lines; also absent: CEACAM5, AGR3, PRR15L; co-absent with the target |
| [[LINC01456]] | C | LINC01456 activity raises SLITRK6's level | lines that do not express LINC01456 (42) vs lines expressing it (8) | 3.40× lower at baseline in the lines without LINC01456 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, CALCA, S100A8; co-absent with the target |
| [[KCNH7]] | C | KCNH7 activity raises SLITRK6's level | lines that do not express KCNH7 (35) vs lines expressing it (15) | 3.25× lower at baseline in the lines without KCNH7 | 0.013 | ⚠ within organs, on part of the lines; also absent: FUT9, ENSG00000289309, PI15; maybe low, not absent; co-absent with the target |
| [[CGA]] | C | CGA activity raises SLITRK6's level | lines that do not express CGA (44) vs lines expressing it (6) | 4.64× lower at baseline in the lines without CGA | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, SYT4, RIT2; co-absent with the target |
| [[ERG]] | C | ERG activity raises SLITRK6's level | lines that do not express ERG (30) vs lines expressing it (20) | 2.86× lower at baseline in the lines without ERG | 0.019 | ⚠ within organs, on part of the lines; also absent: FUT9, ZIC1, MDGA2; maybe low, not absent; co-absent with the target |
| [[IGFBP5]] | C | IGFBP5 activity raises SLITRK6's level | lines that do not express IGFBP5 (34) vs lines expressing it (16) | 3.02× lower at baseline in the lines without IGFBP5 | 0.019 | ⚠ within organs, on part of the lines; also absent: DOK5, MGP, CTNND2; co-absent with the target |
| [[LINC02253]] | C | LINC02253 activity raises SLITRK6's level | lines that do not express LINC02253 (35) vs lines expressing it (15) | 1.91× lower at baseline in the lines without LINC02253 | 0.023 | ⚠ within organs, on part of the lines; also absent: VIL1, LINC02058, ENSG00000289349; co-absent with the target |
| [[PARM1]] | C | PARM1 activity raises SLITRK6's level | lines that do not express PARM1 (27) vs lines expressing it (23) | 2.60× lower at baseline in the lines without PARM1 | 0.023 | ⚠ within organs, on part of the lines; also absent: ST6GAL2, PRR15L, C2CD4A; co-absent with the target |
| [[MGAT4C]] | C | MGAT4C activity raises SLITRK6's level | lines that do not express MGAT4C (35) vs lines expressing it (15) | 2.30× lower at baseline in the lines without MGAT4C | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000281566, LINC01205, ENSG00000286385; co-absent with the target |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 7, C 7. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR4A2]] | B | SLITRK6 activity raises NR4A2's level | lines that do not express SLITRK6 (28) vs lines expressing it (22) | 2.39× lower at baseline in the lines without SLITRK6 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000288098, ENSG00000259692, TENM4 |
| [[LINC01414]] | B | SLITRK6 activity raises LINC01414's level | lines that do not express SLITRK6 (28) vs lines expressing it (22) | 2.01× lower at baseline in the lines without SLITRK6 | 0.049 | ⚠ within organs, on part of the lines; also absent: ENSG00000288098, ENSG00000259692, TENM4 |
| [[NR4A1]] | B | SLITRK6 activity raises NR4A1's level | lines that do not express SLITRK6 (28) vs lines expressing it (22) | 1.75× lower at baseline in the lines without SLITRK6 | 0.064 | ⚠ within organs, on part of the lines; also absent: ENSG00000288098, ENSG00000259692, TENM4 |
| [[NR4A2]] | B | SLITRK6 activity strengthens NR4A2's drug response | lines that do not express SLITRK6 (21) vs lines expressing it (21) | the lines without SLITRK6 respond 0.86× as strongly (z diff +1.20); strongest at Panobinostat 5 µM: 0.63x vs 0.39x (z diff +2.9) | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000288098, ENSG00000259692, TENM4; target measured in part of the lines; the reference differs; artifact flags |
| [[MAPK10]] | B | SLITRK6 activity raises MAPK10's level | lines that do not express SLITRK6 (28) vs lines expressing it (22) | 2.40× lower at baseline in the lines without SLITRK6 | 0.070 | ⚠ within organs, on part of the lines; also absent: ENSG00000288098, ENSG00000259692, TENM4 |
| [[LINC01414]] | B | SLITRK6 activity weakens LINC01414's drug response | lines that do not express SLITRK6 (28) vs lines expressing it (19) | the lines without SLITRK6 respond 6.77× as strongly (z diff -1.70); strongest at Dinaciclib 5 µM: 1.60x vs 0.35x (z diff -6.8) | 0.082 | ⚠ within organs, on part of the lines; also absent: ENSG00000288098, ENSG00000259692, TENM4; target measured in part of the lines; artifact flags |
| [[LINC01695]] | B | SLITRK6 activity raises LINC01695's level | lines that do not express SLITRK6 (28) vs lines expressing it (22) | 2.48× lower at baseline in the lines without SLITRK6 | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000288098, ENSG00000259692, TENM4 |
| [[MIR646HG]] | C | SLITRK6 activity raises MIR646HG's level | lines that do not express SLITRK6 (28) vs lines expressing it (22) | 3.10× lower at baseline in the lines without SLITRK6 | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000288098, ENSG00000259692, TENM4; co-absent with the target |
| [[FSTL5]] | C | SLITRK6 activity raises FSTL5's level | lines that do not express SLITRK6 (28) vs lines expressing it (22) | 3.12× lower at baseline in the lines without SLITRK6 | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000288098, ENSG00000259692, TENM4; co-absent with the target |
| [[TMEM108]] | C | SLITRK6 activity raises TMEM108's level | lines that do not express SLITRK6 (28) vs lines expressing it (22) | 2.82× lower at baseline in the lines without SLITRK6 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000288098, ENSG00000259692, TENM4; co-absent with the target |
| [[VAV3]] | C | SLITRK6 activity raises VAV3's level | lines that do not express SLITRK6 (28) vs lines expressing it (22) | 2.61× lower at baseline in the lines without SLITRK6 | 0.066 | ⚠ within organs, on part of the lines; also absent: ENSG00000288098, ENSG00000259692, TENM4; co-absent with the target |
| [[PDZRN3]] | C | SLITRK6 activity raises PDZRN3's level | lines that do not express SLITRK6 (28) vs lines expressing it (22) | 3.03× lower at baseline in the lines without SLITRK6 | 0.070 | ⚠ within organs, on part of the lines; also absent: ENSG00000288098, ENSG00000259692, TENM4; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.711). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.2, 35.6); signed map (42.3, 34.9). **Vector** length 54.5, 14.4% of its response variance represented; |z| ≥ 3 in 534 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.3 | +8.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.7 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.2 | +6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +5.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | -5.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.1 | +1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | -2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +3.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.7 | +3.0 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -2.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.0 | -2.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.0 | -2.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.9 | -0.5 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.8 | -3.1 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.7 | -2.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | SLIT and NTRK like family member 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q31.1 — chr13:85,792,790-85,806,683 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22774 |
| Gene groups (HGNC) | SLIT and NTRK like family |
| Reactome | 3 pathways, smallest: Receptor-type tyrosine-protein phosphatases; Protein-protein interactions at synapses; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H5Y7](https://www.uniprot.org/uniprotkb/Q9H5Y7) (SLIT and NTRK-like protein 6):

> Regulator of neurite outgrowth required for normal hearing and vision.

**Summary**, from NCBI Gene [84189](https://www.ncbi.nlm.nih.gov/gene/84189):

> This gene encodes a member of the SLITRK protein family. Members of this family are integral membrane proteins that are characterized by two N-terminal leucine-rich repeat (LRR) domains and a C-terminal region that shares homology with trk neurotrophin receptors. This protein functions as a regulator of neurite outgrowth required for normal hearing and vision. Mutations in this gene are a cause of myopia and deafness. [provided by RefSeq, Dec 2014]

**Accessions** — [HGNC:23503](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23503) · Entrez [84189](https://www.ncbi.nlm.nih.gov/gene/84189) · UniProt [Q9H5Y7](https://www.uniprot.org/uniprotkb/Q9H5Y7) · Ensembl [ENSG00000184564](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184564)

## Data

Gene col 11551: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11551); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11551, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11551]; `tensor/DDL_lfc|DDL_z.npy` [11551]; `embed/gene_vectors.npy` [11551]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11551 or target_col == 11551). Every well: [[SLITRK6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLITRK6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
