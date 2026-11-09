---
symbol: "CCNE2"
type: "gene"
col: 10591
ensembl_id: "ENSG00000175305"
name: "cyclin E2"
location: "8q22.1"
module: 6
arm: "+"
pooled_cpm: 9.37
n_lines_expressing: 50
n_dd_up: 38
n_dd_down: 13
n_dd_up_clean: 16
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/006", "written"]
generated_by: "tahoemap"
---

# CCNE2

*cyclin E2* — 8q22.1

> [!summary] In one line
> CCNE2 encodes cyclin E2, a CDK2 partner that accumulates at the G1/S transition and licenses entry into S phase.

## What it is

Cyclin E2 is the second E-type cyclin, sharing CDK2 and its late-G1 window with cyclin E1, and phosphorylating RB and p27. Its transcription is an E2F output, and the protein is degraded by SCF-[[FBXW7]] after autophosphorylation, so both message and protein are sharply cell-cycle periodic. Mice lacking both E cyclins develop surprisingly far: E cyclins are dispensable for ordinary mitotic cycles and needed for endoreplication and re-entry from quiescence, making cyclin E2 a reinforcer rather than the gatekeeper of S phase. It is frequently amplified in cancer, notably breast cancer, where high cyclin E tracks resistance to endocrine and CDK4/6 therapy.

## What is uncertain

Cyclin E2 mRNA is partly a readout of what fraction of cells are in late G1 or S, so "repressed by p53" here may mean no more than arrest; for this class of gene the direct-versus-indirect question resolves as indirect. Redundancy with CCNE1 also means transcript changes do not map cleanly onto CDK2 activity. The circularity warning below applies with full force.

## References

- Lauper et al., 1998, Oncogene — identified cyclin E2 as a CDK2 partner acting in late G1 and S phase.
- Gudas et al., 1999, Molecular and Cellular Biology — characterised cyclin E2 and its aberrant expression in human cancers.
- Geng et al., 2003, Cell — cyclin E1/E2 double-knockout mice show E cyclins are dispensable for normal cycles but needed for endoreplication.
- Litovchick et al., 2007, Molecular Cell — described the DREAM complex repressing cell-cycle-dependent genes.
- Fischer et al., 2016, Nucleic Acids Research — integrated TP53, DREAM and RB-E2F target analyses into cell-cycle gene regulatory networks.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (22 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.92× (z +24.3, q 0e+00, up in 41 of 43 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.93× (z +11.7, q 1e-29, up in 23 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Neratinib (maleate) (drug)]] 5 µM: 0.736× (z -5.5, q 2e-05, down in 17 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM111B]] (+0.87, fdr 7e-06), [[E2F2]] (+0.82, fdr 7e-06), [[E2F1]] (+0.81, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 23 with an alert ⚠; shown: the 15 strongest and the 13 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 22 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10591.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **3.92×** | +24.3 | 0e+00 | 41/43 (SW480, A549, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **3.71×** | +16.5 | 0e+00 | 41/47 (NCI-H2347, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **3.50×** | +15.7 | 0e+00 | 43/47 (A498, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **3.40×** | +15.4 | 0e+00 | 41/47 (A498, PANC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.93×** | +11.7 | 1e-29 | 23/42 (AsPC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **2.46×** | +11.3 | 1e-27 | 32/46 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~57% of this change | **2.51×** | +11.1 | 7e-27 | 26/35 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **2.40×** | +10.6 | 2e-24 | 27/41 (SW480, RKO, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.23×** | +10.1 | 3e-22 | 29/42 (Panc 03.27, PANC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.74×** | +9.8 | 5e-21 | 29/47 (PANC-1, SW480, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **2.17×** | +9.4 | 4e-19 | 26/40 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.92×** | +8.2 | 1e-14 | 16/30 (SNU-423, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.89×** | +7.7 | 6e-13 | 11/18 (SNU-423, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.83×** | +7.6 | 1e-12 | 26/47 (SW480, RKO, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.83×** | +7.6 | 2e-12 | 25/47 (SW1417, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.60×** | +5.9 | 9e-08 | 18/44 (SW480, HT-29, …) | rises with dose |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | **1.38×** | +5.4 | 2e-06 | 16/47 (SW480, RKO, …) | all doses, flat |  |
| [[Cytarabine (drug)]] 0.05 µM |  | **1.50×** | +4.7 | 6e-05 | 11/46 (A-427, J82, …) | all doses, stronger at high dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **1.42×** | +4.1 | 0.001 | 14/46 (A-427, RKO, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.82×** | +3.9 | 0.002 | 8/40 (SW480, J82, …) | top dose only | noisy plate (z scaled) |
| [[Gemcitabine (drug)]] 5 µM |  | **1.47×** | +3.5 | 0.008 | 5/43 (HEC-1-A, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.012 | 10/45 (C32, SW48, …) | top dose only |  |
| [[Gemcitabine (drug)]] 0.5 µM |  | **1.31×** | +3.4 | 0.014 | 7/47 (SW480, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.015 | 9/46 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.024 | 8/44 (BT-474, C32, …) | top dose only |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **1.28×** | +3.1 | 0.033 | 1/47 (PANC-1) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.30×** | +3.0 | 0.045 | 8/41 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.25×** | +2.8 | 0.079 | 6/47 (Panc 03.27, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10591.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.736×** | -5.5 | 2e-05 | 17/48 (Hs 766T, HCT15, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.671×** | -5.1 | 1e-04 | 17/44 (RPMI-7951, HCT15, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.709×** | -4.4 | 0.002 | 20/47 (LS 180, BT-474, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.785×** | -4.4 | 0.002 | 21/47 (KATO III, J82, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.739×** | -3.8 | 0.013 | 11/47 (RKO, SK-MEL-2, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.741×** | -3.8 | 0.013 | 17/44 (C32, A-172, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.817×** | -3.6 | 0.022 | 15/47 (RKO, KATO III, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.829×** | -3.4 | 0.051 | 12/47 (SK-MEL-2, C32, …) | top dose only |  |
| [[Cepharanthine (drug)]] 5 µM |  | **0.832×** | -3.3 | 0.053 | 12/47 (A498, NCI-H1792, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.607×** | -3.3 | 0.053 | 13/36 (Panc 03.27, C32, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.768×** | -3.2 | 0.063 | 9/44 (A-172, KATO III, …) | rises with dose |  |
| [[Rapamycin (drug)]] 0.05 µM |  | **0.785×** | -3.1 | 0.087 | 6/46 (RPMI-7951, A498, …) | inconsistent across doses |  |
| [[Neratinib (drug)]] 5 µM |  | **0.785×** | -3.1 | 0.087 | 11/47 (LoVo, NCI-H2030, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.55 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10591. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 9.94 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.91× (z +13.5) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[A-172 (line)]] | wt | 11.5 | 0 | 2 (1 ⚠) | — | [[Peretinoin (drug)]] 5 µM 0.0857× (z -9.3) |
| [[A498 (line)]] | wt | 6.71 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 6.48× (z +8.7) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[AsPC-1 (line)]] | alt | 3.23 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +10.0) | — |
| [[SW1417 (line)]] | alt | 11.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +9.7) | — |
| [[A549 (line)]] | wt | 3.35 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.7× (z +13.0) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[CFPAC-1 (line)]] | alt | 5.29 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.04× (z +9.1) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[HCT15 (line)]] | alt | 16.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 7.83 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.20× (z +8.8) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[HS-578T (line)]] | alt | 8.59 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.67× (z +8.7) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[HT-29 (line)]] | alt | 7.24 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.73× (z +9.9) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[LoVo (line)]] | wt | 5.00 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.24× (z +9.4) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[LOX-IMVI (line)]] | wt | 4.83 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.48× (z +8.5) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 5.25 | 0 | 1 | — | [[Alpelisib (drug)]] 0.05 µM 0.0635× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 10.3 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.87× (z +10.8) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H460 (line)]] | wt | 4.85 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.76× (z +9.3) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[Panc 03.27 (line)]] | alt | 8.79 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.52× (z +10.3) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[PANC-1 (line)]] | alt | 6.11 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.62× (z +12.4) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[SW 900 (line)]] | alt | 6.90 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.39× (z +8.6) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[A-427 (line)]] | wt | 9.13 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.88 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.99 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.32 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.67 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10591), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM111B]] | +0.87 | +0.82 / +0.89 | both halves | 7e-06 | **novel candidate** |
| [[E2F2]] | +0.82 | +0.74 / +0.83 | both halves | 7e-06 | pathway: Aberrant regulation of mitotic G1/S transition in cancer due to RB1 defects; STRING 845 |
| [[E2F1]] | +0.81 | +0.76 / +0.85 | both halves | 7e-06 | pathway: Aberrant regulation of mitotic G1/S transition in cancer due to RB1 defects; STRING 883 |
| [[CLSPN]] | +0.80 | +0.72 / +0.85 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[MCM10]] | +0.79 | +0.73 / +0.82 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 825 |
| [[CDC6]] | +0.78 | +0.75 / +0.81 | both halves | 7e-06 | pathway: CDK-mediated phosphorylation and removal of Cdc6; STRING 931 |
| [[ZNF367]] | +0.77 | +0.68 / +0.82 | both halves | 7e-06 |  |
| [[GINS2]] | +0.77 | +0.63 / +0.87 | both halves | 7e-06 | pathway: DNA Replication; STRING 409 |
| [[EXO1]] | +0.76 | +0.68 / +0.82 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 596 |
| [[DTL]] | +0.76 | +0.66 / +0.81 | both halves | 7e-06 | STRING 571 |
| [[ASF1B]] | +0.76 | +0.69 / +0.77 | both halves | 7e-06 |  |
| [[WDR76]] | +0.75 | +0.68 / +0.81 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CCNE2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TOP1]] | B | TOP1 activity lowers CCNE2's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 5.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CDC25A]] | B | CDC25A activity raises CCNE2's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 1.83× lower at baseline in the lines without CDC25A | 0.099 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[MYBL2]] | C | MYBL2 activity raises CCNE2's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 2.13× lower at baseline in the lines without MYBL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.751). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-35.7, -45.0); signed map (-38.5, -45.6). **Vector** length 103, 25.8% of its response variance represented; |z| ≥ 3 in 1,259 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.58 to 65); *DNA strand elongation* (reactome, mean cos +0.62 to 28); *Activation of the pre-replicative complex* (reactome, mean cos +0.64 to 22).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +6.8 | +24.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +5.6 | +11.3 |
|  | [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | +4.2 | +7.3 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | +4.2 | +6.0 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | +4.1 | +7.6 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +3.4 | +4.1 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +3.2 | +4.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.8 | +3.9 |
|  | [[Raltitrexed (drug)]] 0.5 µM |  | +2.4 | +5.9 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | +2.4 | +5.4 |
| fall | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | -3.6 | -3.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -0.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.4 | -2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.2 | -4.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.1 | -5.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -0.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.8 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | cyclin E2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.1 — chr8:94,879,770-94,896,678 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CYCE2 |
| Gene groups (HGNC) | Cyclins |
| Reactome | 34 pathways, smallest: Phosphorylation of proteins involved in G1/S transition by active Cyclin E:Cdk2 complexes; TP53 Regulates Transcription of Genes Involved in G1 Cell Cycle Arrest; Aberrant regulation of mitotic G1/S transition in cancer due to RB1 defects |
| Matched by | ensembl_id |

**Function**, from UniProt [O96020](https://www.uniprot.org/uniprotkb/O96020) (G1/S-specific cyclin-E2):

> Essential for the control of the cell cycle at the late G1 and early S phase.

**Summary**, from NCBI Gene [9134](https://www.ncbi.nlm.nih.gov/gene/9134):

> The protein encoded by this gene belongs to the highly conserved cyclin family, whose members are characterized by a dramatic periodicity in protein abundance through the cell cycle. Cyclins function as regulators of CDK kinases. Different cyclins exhibit distinct expression and degradation patterns which contribute to the temporal coordination of each mitotic event. This cyclin forms a complex with and functions as a regulatory subunit of CDK2. This cyclin has been shown to specifically …

**Accessions** — [HGNC:1590](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1590) · Entrez [9134](https://www.ncbi.nlm.nih.gov/gene/9134) · UniProt [O96020](https://www.uniprot.org/uniprotkb/O96020) · Ensembl [ENSG00000175305](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175305)

## Data

Gene col 10591: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10591); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10591, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10591]; `tensor/DDL_lfc|DDL_z.npy` [10591]; `embed/gene_vectors.npy` [10591]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10591 or target_col == 10591). Every well: [[CCNE2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/CCNE2.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
