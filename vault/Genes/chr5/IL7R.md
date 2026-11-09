---
symbol: "IL7R"
type: "gene"
col: 9684
ensembl_id: "ENSG00000168685"
name: "interleukin 7 receptor"
location: "5p13.2"
module: 202
arm: "+"
pooled_cpm: 12.6
n_lines_expressing: 20
n_dd_up: 31
n_dd_down: 6
n_dd_up_clean: 20
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 16
direction_downstream: 21
tags: ["gene", "module/202"]
generated_by: "tahoemap"
---

# IL7R

*interleukin 7 receptor* — 5p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 6.35× (z +22.6, q 0e+00, up in 18 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.440× (z -7.1, q 7e-10, down in 18 of 18 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCN3A]] (+0.68, fdr 7e-06), [[FGF2]] (+0.65, fdr 1e-05), [[CACNA2D1]] (+0.65, fdr 4e-05); moves opposite to [[SDHAP1]] (-0.57, fdr 2e-05), [[SDHAP2]] (-0.57, fdr 3e-05), [[SMARCD2]] (-0.56, fdr 4e-05).
> It is in [[Module 202]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[TRIP6]] → it (grade B ⚠); 21 go from it, the strongest it → [[PMAIP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9684.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **6.35×** | +22.6 | 0e+00 | 18/18 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **6.91×** | +16.7 | 0e+00 | 18/18 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **7.04×** | +16.2 | 0e+00 | 18/18 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **4.64×** | +13.2 | 7e-38 | 18/18 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **4.23×** | +12.5 | 2e-33 | 10/15 (J82, SW 900, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **3.47×** | +10.7 | 7e-25 | 17/18 (HOP62, SW 900, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **3.14×** | +9.5 | 2e-19 | 6/13 (J82, SNU-423, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.13×** | +9.2 | 3e-18 | 17/18 (HOP62, SW 900, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.06×** | +8.8 | 9e-17 | 10/18 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.53×** | +8.0 | 7e-14 | 15/18 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.28×** | +6.6 | 3e-09 | 7/13 (Hs 766T, J82, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.96×** | +5.8 | 3e-07 | 6/17 (NCI-H460, HOP62, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +5.3 | 4e-06 | 8/18 (HOP62, Panc 03.27, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +4.8 | 5e-05 | 6/16 (HS-578T, A498, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.72×** | +4.7 | 1e-04 | 9/18 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.77×** | +4.7 | 1e-04 | 11/18 (HOP62, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.67×** | +4.4 | 3e-04 | 9/18 (HOP62, A-172, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.56×** | +3.8 | 0.003 | 8/18 (HOP62, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Isocorydine (drug)]] 0.5 µM |  | **1.52×** | +3.6 | 0.009 | 7/18 (NCI-H1792, J82, …) | two highest doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.51×** | +3.6 | 0.010 | 12/18 (HOP62, SW 900, …) | rises with dose | cell-cycle shift (explains ~9% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9684.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.440×** | -7.1 | 7e-10 | 18/18 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.489×** | -6.2 | 2e-07 | 16/18 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.514×** | -5.8 | 2e-06 | 17/18 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.616×** | -4.2 | 0.004 | 14/18 (A-172, NCI-H460, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.723×** | -4.0 | 0.007 | 10/18 (H4, A-172, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.666×** | -3.5 | 0.039 | 8/18 (J82, HS-578T, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.708× | -3.0 | 0.21 | 4/18 (NCI-H460, SW 1271, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9684. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 141 | 5 | 3 | [[Homoharringtonine (drug)]] 5 µM 8.55× (z +16.8) | [[Panobinostat (drug)]] 0.5 µM 0.0622× (z -15.5) |
| [[HOP62 (line)]] | alt | 23.6 | 7 | 1 | [[Homoharringtonine (drug)]] 5 µM 31.6× (z +24.6) | [[Panobinostat (drug)]] 0.5 µM 0.181× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 25.6 | 5 | 3 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +19.0) | [[Panobinostat (drug)]] 0.5 µM 0.122× (z -12.4) |
| [[A498 (line)]] | wt | 6.50 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.66× (z +10.3) | [[Selinexor (drug)]] 5 µM 0.208× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 105 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +10.7) | [[Panobinostat (drug)]] 0.5 µM 0.145× (z -12.0) |
| [[SW 900 (line)]] | alt | 14.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.39× (z +11.5) | — |
| [[HS-578T (line)]] | alt | 11.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.4× (z +14.7) | — |
| [[hTERT-HPNE (line)]] | wt | 34.0 | 3 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 8.78× (z +10.0) | [[Panobinostat (drug)]] 5 µM 0.112× (z -10.1) |
| [[SNU-423 (line)]] | alt | 5.40 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 43.6× (z +15.2) | — |
| [[H4 (line)]] | wt | 70.9 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.128× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 6.99 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 9.53× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.0647× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 5.14 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 38.6× (z +11.2) | — |
| [[Hs 766T (line)]] | wt | 10.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +10.8) | — |
| [[NCI-H1792 (line)]] | alt | 31.4 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 7.68× (z +10.2) | — |
| [[A-427 (line)]] | wt | 0.654 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.981 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.21 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.849 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.985 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.870 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.846 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.930 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.873 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.690 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.42 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.758 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.846 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.885 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.966 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.08 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9684), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCN3A]] | +0.68 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[FGF2]] | +0.65 | +0.66 / +0.50 | both halves | 1e-05 | STRING 591 |
| [[CACNA2D1]] | +0.65 | +0.64 / +0.42 | both halves | 4e-05 |  |
| [[LY6K]] | +0.65 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[SLFN12]] | +0.65 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[ABCC9]] | +0.65 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[TENM3-AS1]] | +0.64 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[SALL1]] | +0.63 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[OFCC1]] | +0.62 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[TNIP3]] | +0.62 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[TRIML2]] | +0.62 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[SYNPO]] | +0.61 | +0.62 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAP1]] | -0.57 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[SDHAP2]] | -0.57 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[SMARCD2]] | -0.56 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[CBFA2T2]] | -0.56 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[PDPR2P]] | -0.55 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[TAF5L]] | -0.55 | -0.48 / -0.36 | both halves | 9e-05 |  |
| [[SOCS7]] | -0.55 | -0.50 / -0.43 | both halves | 4e-05 |  |
| [[A1BG]] | -0.54 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[GMCL1]] | -0.54 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[LCMT1]] | -0.54 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[ZNF667-AS1]] | -0.53 | -0.49 / -0.24 | both halves | 5e-04 |  |
| [[MTMR12]] | -0.53 | -0.49 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 3, C 13. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRIP6]] | B | TRIP6 activity raises IL7R's level | lines that do not express TRIP6 (12) vs lines expressing it (38) | 2.97× lower at baseline in the lines without TRIP6 | 0.013 | ⚠ within organs, on part of the lines; also absent: EFNB2, PLAC4 |
| [[TOP2A]] | B | TOP2A activity lowers IL7R's level | compounds that target TOP2A: 4 of 5 raise it (Amsacrine, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises IL7R's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PLPP4]] | C | PLPP4 activity raises IL7R's level | lines that do not express PLPP4 (31) vs lines expressing it (19) | 5.75× lower at baseline in the lines without PLPP4 | 0.006 | ⚠ within organs, on part of the lines; also absent: GYPC, LINC02930, TNFAIP6; co-absent with the target |
| [[ABCC9]] | C | ABCC9 activity raises IL7R's level | lines that do not express ABCC9 (28) vs lines expressing it (22) | 4.69× lower at baseline in the lines without ABCC9 | 0.007 | ⚠ within organs, on part of the lines; also absent: WNT5A, PDGFRB, CCL3; maybe low, not absent; co-absent with the target |
| [[FLRT2]] | C | FLRT2 activity raises IL7R's level | lines that do not express FLRT2 (29) vs lines expressing it (21) | 4.28× lower at baseline in the lines without FLRT2 | 0.012 | ⚠ within organs, on part of the lines; also absent: KCNMA1, FLI1, IL13RA2; co-absent with the target |
| [[ZEB2]] | C | ZEB2 activity raises IL7R's level | lines that do not express ZEB2 (27) vs lines expressing it (23) | 4.91× lower at baseline in the lines without ZEB2 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADAM12, LINC01583, PRR16; co-absent with the target |
| [[LINC02930]] | C | LINC02930 activity raises IL7R's level | lines that do not express LINC02930 (33) vs lines expressing it (17) | 3.89× lower at baseline in the lines without LINC02930 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000232053, GYPC, PLPP4; co-absent with the target |
| [[TLR4]] | C | TLR4 activity raises IL7R's level | lines that do not express TLR4 (26) vs lines expressing it (24) | 3.38× lower at baseline in the lines without TLR4 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ENSG00000287335, FLI1, ABI3BP; co-absent with the target |
| [[CCL3]] | C | CCL3 activity raises IL7R's level | lines that do not express CCL3 (37) vs lines expressing it (13) | 6.79× lower at baseline in the lines without CCL3 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMPRSS15, ENSG00000224865, ESM1; co-absent with the target |
| [[SYNPO]] | C | SYNPO activity raises IL7R's level | lines that do not express SYNPO (15) vs lines expressing it (35) | 3.47× lower at baseline in the lines without SYNPO | 0.060 | ⚠ within organs, on part of the lines; also absent: GLIS3, ENSG00000261227, ADAM7-AS1; maybe low, not absent; co-absent with the target |
| [[LINC01828]] | C | LINC01828 activity raises IL7R's level | lines that do not express LINC01828 (17) vs lines expressing it (33) | 3.69× lower at baseline in the lines without LINC01828 | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000253471, ENSG00000230647, ENSG00000253891; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 8, C 13. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PMAIP1]] | B | IL7R activity raises PMAIP1's level | lines that do not express IL7R (30) vs lines expressing it (20) | 2.05× lower at baseline in the lines without IL7R | 0.010 | ⚠ within organs, on part of the lines; also absent: IL1B, COL5A1, CCBE1 |
| [[TRIP6]] | B | IL7R activity raises TRIP6's level | lines that do not express IL7R (30) vs lines expressing it (20) | 2.14× lower at baseline in the lines without IL7R | 0.013 | ⚠ within organs, on part of the lines; also absent: IL1B, COL5A1, CCBE1 |
| [[ATP10D]] | B | IL7R activity raises ATP10D's level | lines that do not express IL7R (30) vs lines expressing it (20) | 2.40× lower at baseline in the lines without IL7R | 0.024 | ⚠ within organs, on part of the lines; also absent: IL1B, COL5A1, CCBE1 |
| cells under [[Naproxen (drug)]] 5 µM | B | IL7R activity raises the cells' numbers under Naproxen 5 µM (protects the cells) | lines that do not express IL7R (30) vs lines expressing it (18) | the lines without IL7R: 0.81× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: IL1B, COL5A1, CCBE1 |
| [[LHFPL6]] | B | IL7R activity raises LHFPL6's level | lines that do not express IL7R (30) vs lines expressing it (20) | 3.21× lower at baseline in the lines without IL7R | 0.079 | ⚠ within organs, on part of the lines; also absent: IL1B, COL5A1, CCBE1 |
| cells under [[Tucatinib (drug)]] 5 µM | B | IL7R activity raises the cells' numbers under Tucatinib 5 µM (protects the cells) | lines that do not express IL7R (30) vs lines expressing it (18) | the lines without IL7R: 0.83× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: IL1B, COL5A1, CCBE1 |
| cells under [[Tirabrutinib (hydrochloride) (drug)]] 0.05 µM | B | IL7R activity raises the cells' numbers under Tirabrutinib (hydrochloride) 0.05 µM (protects the cells) | lines that do not express IL7R (30) vs lines expressing it (18) | the lines without IL7R: 0.83× the cells of the other lines | 0.086 | ⚠ within organs, on part of the lines; also absent: IL1B, COL5A1, CCBE1 |
| cells under [[Irinotecan (hydrochloride) (drug)]] 5 µM | B | IL7R activity raises the cells' numbers under Irinotecan (hydrochloride) 5 µM (protects the cells) | lines that do not express IL7R (30) vs lines expressing it (18) | the lines without IL7R: 0.82× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: IL1B, COL5A1, CCBE1 |
| [[FLRT2]] | C | IL7R activity raises FLRT2's level | lines that do not express IL7R (30) vs lines expressing it (20) | 6.04× lower at baseline in the lines without IL7R | 0.002 | ⚠ within organs, on part of the lines; also absent: IL1B, COL5A1, CCBE1; co-absent with the target |
| [[ZNF469]] | C | IL7R activity raises ZNF469's level | lines that do not express IL7R (30) vs lines expressing it (20) | 4.18× lower at baseline in the lines without IL7R | 0.010 | ⚠ within organs, on part of the lines; also absent: IL1B, COL5A1, CCBE1; co-absent with the target |
| [[S1PR3]] | C | IL7R activity raises S1PR3's level | lines that do not express IL7R (30) vs lines expressing it (20) | 3.90× lower at baseline in the lines without IL7R | 0.012 | ⚠ within organs, on part of the lines; also absent: IL1B, COL5A1, CCBE1; co-absent with the target |
| [[LINC00702]] | C | IL7R activity raises LINC00702's level | lines that do not express IL7R (30) vs lines expressing it (20) | 3.23× lower at baseline in the lines without IL7R | 0.024 | ⚠ within organs, on part of the lines; also absent: IL1B, COL5A1, CCBE1; co-absent with the target |

## Where it sits

- **Module**: [[Module 202]]; 15 genes; every member is in the + arm (projection on the module's main direction 0.773). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (35.0, 24.0); signed map (44.9, 24.4). **Vector** length 74.4, 23.6% of its response variance represented; |z| ≥ 3 in 615 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.7 | +22.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.8 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +5.6 | +12.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +5.5 | +9.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.3 | +16.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +10.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +5.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +8.0 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.1 | -6.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.8 | -7.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.7 | -5.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.2 | -4.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.9 | -0.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.4 | -1.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.4 | -2.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.4 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | interleukin 7 receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p13.2 — chr5:35,852,695-35,879,603 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CD127, IL7RA, lnc-IL7R, IL-7Ralpha, IL7Ralpha, sIL-7R, CDw127 |
| Gene groups (HGNC) | CD molecules; Fibronectin type III domain containing; Interleukin receptors |
| Hallmark sets | INFLAMMATORY_RESPONSE, KRAS_SIGNALING_UP, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 7 pathways, smallest: Interleukin-7 signaling; Cargo recognition for clathrin-mediated endocytosis; Clathrin-mediated endocytosis |
| Matched by | ensembl_id |

**Function**, from UniProt [P16871](https://www.uniprot.org/uniprotkb/P16871) (Interleukin-7 receptor subunit alpha):

> Receptor for interleukin-7. Also acts as a receptor for thymic stromal lymphopoietin (TSLP).

**Summary**, from NCBI Gene [3575](https://www.ncbi.nlm.nih.gov/gene/3575):

> The protein encoded by this gene is a receptor for interleukin 7 (IL7). The function of this receptor requires the interleukin 2 receptor, gamma chain (IL2RG), which is a common gamma chain shared by the receptors of various cytokines, including interleukins 2, 4, 7, 9, and 15. This protein has been shown to play a critical role in V(D)J recombination during lymphocyte development. Defects in this gene may be associated with severe combined immunodeficiency (SCID). Alternatively spliced …

**Accessions** — [HGNC:6024](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6024) · Entrez [3575](https://www.ncbi.nlm.nih.gov/gene/3575) · UniProt [P16871](https://www.uniprot.org/uniprotkb/P16871) · Ensembl [ENSG00000168685](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168685)

## Data

Gene col 9684: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9684); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9684, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9684]; `tensor/DDL_lfc|DDL_z.npy` [9684]; `embed/gene_vectors.npy` [9684]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9684 or target_col == 9684). Every well: [[IL7R — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IL7R.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
