---
symbol: "CA2"
type: "gene"
col: 2433
ensembl_id: "ENSG00000104267"
name: "carbonic anhydrase 2"
location: "8q21.2"
module: 81
arm: "+"
pooled_cpm: 12.93
n_lines_expressing: 23
n_dd_up: 21
n_dd_down: 2
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 5
direction_downstream: 7
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# CA2

*carbonic anhydrase 2* — 8q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.42× (z +20.5, q 0e+00, up in 11 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.656× (z -4.0, q 0.039, down in 11 of 19 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (LS 180 0.185×); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (NCI-H1573 0.0481×); [[Panobinostat (drug)]] 5 µM in 1 line (LS 180 0.194×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRDM8]] (+0.59, fdr 1e-05), [[GTF2IP7]] (+0.59, fdr 1e-05), [[TFF1]] (+0.58, fdr 1e-05); moves opposite to [[RHEX]] (-0.42, fdr 2e-04), [[ANP32B]] (-0.41, fdr 1e-04).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 7 go from it, the strongest it → [[INO80C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2433.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.42×** | +20.5 | 0e+00 | 11/19 (HEC-1-A, LoVo, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.06×** | +15.2 | 0e+00 | 5/9 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.49×** | +14.7 | 0e+00 | 11/15 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.86×** | +14.5 | 1e-45 | 10/20 (A498, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.77×** | +13.0 | 2e-36 | 11/20 (HEC-1-A, HCT15, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.10×** | +10.3 | 1e-22 | 16/21 (NCI-H2347, HEC-1-A, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.82×** | +9.7 | 2e-20 | 13/20 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.56×** | +8.5 | 2e-15 | 7/13 (LoVo, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.07×** | +6.8 | 5e-10 | 7/17 (LoVo, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.99×** | +6.7 | 1e-09 | 12/19 (RKO, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +4.6 | 2e-04 | 3/18 (HEC-1-A, LoVo, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.29×** | +4.2 | 0.001 | 3/14 (LoVo, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **1.44×** | +3.5 | 0.018 | 2/18 (NCI-H1573, HCT15) | inconsistent across doses | low cells (technical?) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.95×** | +3.4 | 0.028 | 2/10 (HCT15, A498) | inconsistent across doses | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.050 | 5/21 (HEC-1-A, RKO, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +3.2 | 0.050 | 6/19 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Vilanterol (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.062 | 6/21 (NCI-H2030, NCI-H460, …) | rises with dose |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 5 µM |  | **1.36×** | +3.0 | 0.077 | 6/21 (LS 180, NCI-H1792, …) | rises with dose |  |
| [[Vilanterol (drug)]] 0.5 µM |  | **1.36×** | +3.0 | 0.080 | 6/19 (LoVo, KATO III, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2433.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (LS 180 0.185×); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (NCI-H1573 0.0481×); [[Panobinostat (drug)]] 5 µM in 1 line (LS 180 0.194×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.656×** | -4.0 | 0.039 | 11/19 (CFPAC-1, NCI-H2030, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.690×** | -3.6 | 0.099 | 10/22 (AsPC-1, NCI-H2030, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 0.706× | -3.4 | 0.11 | 9/21 (NCI-H460, NCI-H2030, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.750× | -3.4 | 0.11 | 9/19 (AsPC-1, LS 180, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.776× | -3.1 | 0.17 | 8/19 (AsPC-1, LS 180, …) | all doses, flat | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.800× | -3.1 | 0.17 | 11/20 (NCI-H2030, LS 180, …) | top dose only | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | 0.801× | -3.1 | 0.18 | 8/21 (AsPC-1, LS 180, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 0.723× | -3.0 | 0.18 | 11/19 (AsPC-1, NCI-H2030, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2433. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 68.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.80× (z +15.9) | — |
| [[A549 (line)]] | wt | 7.41 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.37× (z +10.6) | — |
| [[HEC-1-A (line)]] | alt | 5.67 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.9× (z +15.8) | — |
| [[LS 180 (line)]] | wt | 25.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -12.3) |
| [[CFPAC-1 (line)]] | alt | 11.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.83× (z +12.8) | — |
| [[HCT15 (line)]] | alt | 16.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.77× (z +9.1) | — |
| [[LoVo (line)]] | wt | 9.29 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.67× (z +15.1) | — |
| [[NCI-H1573 (line)]] | alt | 3.65 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.05 µM 0.0481× (z -10.0) |
| [[A-172 (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.72 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.907 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.62 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 65.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.863 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 88.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 43.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 8.12 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.930 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.829 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.00 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.67 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.45 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.14 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2433), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRDM8]] | +0.59 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[GTF2IP7]] | +0.59 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[TFF1]] | +0.58 | +0.56 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE |
| [[C6orf141]] | +0.55 | +0.54 / +0.46 | both halves | 2e-05 |  |
| [[HAS3]] | +0.54 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[IL23A]] | +0.53 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[SERPINB9]] | +0.51 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[AADAC]] | +0.51 | +0.60 / +0.40 | both halves | 5e-05 |  |
| [[PHLDA1]] | +0.51 | +0.52 / +0.48 | both halves | 2e-05 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[FAM107B]] | +0.51 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[TRPV3]] | +0.50 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[HCG20]] | +0.50 | +0.42 / +0.51 | both halves | 4e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RHEX]] | -0.42 | -0.42 / -0.31 | both halves | 2e-04 |  |
| [[ANP32B]] | -0.41 | -0.36 / -0.45 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises CA2's level | compounds that target MAP2K1: 2 of 4 lower it (Cobimetinib, Trametinib) | 50% of the class's compounds vs 0.6% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[AADAC]] | C | AADAC activity raises CA2's level | lines that do not express AADAC (34) vs lines expressing it (16) | 3.13× lower at baseline in the lines without AADAC | 0.029 | ⚠ within organs, on part of the lines; also absent: AADACP1, SUCNR1, LINC01610; co-absent with the target |
| [[SULT2B1]] | C | SULT2B1 activity raises CA2's level | lines that do not express SULT2B1 (28) vs lines expressing it (22) | 2.60× lower at baseline in the lines without SULT2B1 | 0.048 | ⚠ within organs, on part of the lines; also absent: ATP2C2, ST14, SGPP2; maybe low, not absent; co-absent with the target |
| [[AADACP1]] | C | AADACP1 activity raises CA2's level | lines that do not express AADACP1 (32) vs lines expressing it (18) | 2.70× lower at baseline in the lines without AADACP1 | 0.048 | ⚠ within organs, on part of the lines; co-absent genes; also absent: AADAC, SLC19A3, IGFN1; co-absent with the target |
| [[IL1RL1]] | C | IL1RL1 activity raises CA2's level | lines that do not express IL1RL1 (32) vs lines expressing it (18) | 1.72× lower at baseline in the lines without IL1RL1 | 0.053 | ⚠ within organs, on part of the lines; also absent: FAM83A, GSDMC, IGFBP1; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 3, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[INO80C]] | B | CA2 activity raises INO80C's level | lines that do not express CA2 (27) vs lines expressing it (23) | 1.43× lower at baseline in the lines without CA2 | 0.036 | ⚠ within organs, on part of the lines; also absent: CCDC68, SCEL, MUC4 |
| [[ITPRID2]] | B | CA2 activity raises ITPRID2's level | lines that do not express CA2 (27) vs lines expressing it (23) | 1.80× lower at baseline in the lines without CA2 | 0.040 | ⚠ within organs, on part of the lines; also absent: CCDC68, SCEL, MUC4 |
| [[AADACL2-AS1]] | B | CA2 activity raises AADACL2-AS1's level | lines that do not express CA2 (27) vs lines expressing it (23) | 1.46× lower at baseline in the lines without CA2 | 0.045 | ⚠ within organs, on part of the lines; also absent: CCDC68, SCEL, MUC4 |
| [[IL1RL1]] | C | CA2 activity raises IL1RL1's level | lines that do not express CA2 (27) vs lines expressing it (23) | 2.03× lower at baseline in the lines without CA2 | 0.031 | ⚠ within organs, on part of the lines; also absent: CCDC68, SCEL, MUC4; co-absent with the target |
| [[LAMC2]] | C | CA2 activity raises LAMC2's level | lines that do not express CA2 (27) vs lines expressing it (23) | 3.45× lower at baseline in the lines without CA2 | 0.032 | ⚠ within organs, on part of the lines; also absent: CCDC68, SCEL, MUC4; co-absent with the target |
| [[AADACP1]] | C | CA2 activity raises AADACP1's level | lines that do not express CA2 (27) vs lines expressing it (23) | 2.65× lower at baseline in the lines without CA2 | 0.069 | ⚠ within organs, on part of the lines; also absent: CCDC68, SCEL, MUC4; co-absent with the target |
| [[SERPINB9]] | C | CA2 activity raises SERPINB9's level | lines that do not express CA2 (27) vs lines expressing it (23) | 2.57× lower at baseline in the lines without CA2 | 0.088 | ⚠ within organs, on part of the lines; also absent: CCDC68, SCEL, MUC4; co-absent with the target |

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.555). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (43.7, 16.2); signed map (17.7, 54.5). **Vector** length 59.7, 16.0% of its response variance represented; |z| ≥ 3 in 568 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +14.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +15.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +10.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.3 | +6.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +20.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +13.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +1.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.5 | +2.5 |
| fall | [[Budesonide (drug)]] 5 µM |  | -1.9 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -2.7 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -1.8 | -3.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | -3.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.6 | -2.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | carbonic anhydrase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.2 — chr8:85,463,968-85,481,493 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Car2, CA-II, CAII |
| Gene groups (HGNC) | Carbonic anhydrases |
| Hallmark sets | FATTY_ACID_METABOLISM, UV_RESPONSE_UP, XENOBIOTIC_METABOLISM, COMPLEMENT, KRAS_SIGNALING_UP, IL2_STAT5_SIGNALING, HEME_METABOLISM, ESTROGEN_RESPONSE_LATE |
| Reactome | 4 pathways, smallest: Erythrocytes take up carbon dioxide and release oxygen; O2/CO2 exchange in erythrocytes; Reversible hydration of carbon dioxide |
| Matched by | ensembl_id |

**Function**, from UniProt [P00918](https://www.uniprot.org/uniprotkb/P00918) (Carbonic anhydrase 2):

> Catalyzes the reversible hydration of carbon dioxide. Can also hydrate cyanamide to urea. Stimulates the chloride-bicarbonate exchange activity of SLC26A6. Essential for bone resorption and osteoclast differentiation. Involved in the regulation of fluid secretion into the anterior chamber of the eye. Contributes to intracellular pH regulation in the duodenal upper villous epithelium during proton-coupled peptide absorption.

**Summary**, from NCBI Gene [760](https://www.ncbi.nlm.nih.gov/gene/760):

> The protein encoded by this gene is one of several isozymes of carbonic anhydrase, which catalyzes reversible hydration of carbon dioxide. Defects in this enzyme are associated with osteopetrosis and renal tubular acidosis. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jun 2014]

**Accessions** — [HGNC:1373](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1373) · Entrez [760](https://www.ncbi.nlm.nih.gov/gene/760) · UniProt [P00918](https://www.uniprot.org/uniprotkb/P00918) · Ensembl [ENSG00000104267](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104267)

## Data

Gene col 2433: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2433); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2433, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2433]; `tensor/DDL_lfc|DDL_z.npy` [2433]; `embed/gene_vectors.npy` [2433]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2433 or target_col == 2433). Every well: [[CA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
