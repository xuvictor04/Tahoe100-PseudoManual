---
symbol: "PGK1"
type: "gene"
col: 2219
ensembl_id: "ENSG00000102144"
name: "phosphoglycerate kinase 1"
location: "Xq21.1"
module: 99
arm: "+"
pooled_cpm: 691.04
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 25
n_dd_up_clean: 4
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/099"]
generated_by: "tahoemap"
---

# PGK1

*phosphoglycerate kinase 1* — Xq21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 1.81× (z +5.9, q 2e-06, up in 39 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.209× (z -41.6, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ENO1]] (+0.79, fdr 7e-06), [[ALDOA]] (+0.78, fdr 7e-06), [[LDHA]] (+0.74, fdr 7e-06); moves opposite to [[UPF3A]] (-0.65, fdr 7e-06), [[ZBTB8A]] (-0.63, fdr 3e-05), [[ITPA]] (-0.62, fdr 4e-05).
> It is in [[Module 099]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2219.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.81×** | +5.9 | 2e-06 | 39/49 (NCI-H23, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.58×** | +4.5 | 0.002 | 38/48 (SHP-77, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.15× | +3.7 | 0.029 | 16/48 (RKO, SW480, …) | rises with dose |  |
| [[Roxadustat (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.029 | 24/48 (HepG2/C3A, SNU-423, …) | top dose only |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.029 | 24/49 (SNU-423, Hs 766T, …) | top dose only | plate-row cell shift |
| [[Fumaric acid (drug)]] 5 µM |  | 1.20× | +3.3 | 0.095 | 23/49 (HepG2/C3A, RPMI-7951, …) | top dose only | plate-row cell shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.29× | +3.2 | 0.11 | 31/47 (SK-MEL-2, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2219.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.209×** | -41.6 | 0e+00 | 48/48 (H4, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.277×** | -23.2 | 0e+00 | 48/48 (AsPC-1, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.282×** | -20.3 | 0e+00 | 48/48 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.386×** | -17.2 | 0e+00 | 45/47 (RPMI-7951, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.539×** | -16.4 | 0e+00 | 45/49 (C32, HT-29, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.450×** | -14.4 | 3e-45 | 46/47 (RPMI-7951, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.575×** | -10.4 | 2e-23 | 47/48 (C32, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.746×** | -7.7 | 7e-13 | 39/48 (SNU-423, A-172, …) | rises with dose | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.665×** | -7.4 | 1e-11 | 43/48 (H4, C32, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.790×** | -6.2 | 3e-08 | 31/48 (SNU-1, SNU-423, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.539×** | -6.1 | 7e-08 | 45/49 (BT-474, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.734×** | -5.8 | 3e-07 | 36/48 (C32, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.751×** | -5.4 | 3e-06 | 29/48 (C32, HEC-1-A, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.751×** | -5.4 | 3e-06 | 37/48 (CFPAC-1, C-33 A, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.752×** | -5.1 | 1e-05 | 37/50 (CFPAC-1, RPMI-7951, …) | rises with dose | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.775×** | -4.8 | 7e-05 | 32/48 (NCI-H2347, HOP62, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.844× | -4.5 | 3e-04 | 22/48 (BT-474, HOP62, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.822×** | -3.6 | 0.007 | 26/48 (LOX-IMVI, CFPAC-1, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 5 µM |  | **0.727×** | -3.1 | 0.045 | 34/49 (HEC-1-A, HS-578T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.731×** | -3.1 | 0.051 | 27/50 (BT-474, SNU-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | 0.850× | -3.0 | 0.056 | 22/49 (AsPC-1, A-172, …) | inconsistent across doses |  |
| [[MK-3903 (drug)]] 5 µM |  | **0.735×** | -3.0 | 0.056 | 29/48 (NCI-H1573, HCT15, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2219. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 826 | 6 (6 ⚠) | 8 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.10× (z +15.5) ⚠ cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -23.3) |
| [[BT-474 (line)]] | alt | 473 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -33.7) |
| [[C32 (line)]] | wt | 918 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -28.0) |
| [[NCI-H2347 (line)]] | alt | 774 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -35.6) |
| [[PANC-1 (line)]] | alt | 599 | 2 (1 ⚠) | 7 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.19× (z +13.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 2.91× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -39.6) |
| [[RKO (line)]] | wt | 693 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -27.4) |
| [[RPMI-7951 (line)]] | alt | 1,444 | 1 | 8 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 2.95× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -37.4) |
| [[HEC-1-A (line)]] | alt | 564 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -33.0) |
| [[hTERT-HPNE (line)]] | wt | 565 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -23.4) |
| [[NCI-H1573 (line)]] | alt | 730 | 2 (2 ⚠) | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.62× (z +11.7) ⚠ cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -35.1) |
| [[SW 900 (line)]] | alt | 490 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -36.2) |
| [[C-33 A (line)]] | alt | 501 | 1 (1 ⚠) | 6 (2 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.02× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -33.0) |
| [[H4 (line)]] | wt | 839 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -43.6) |
| [[HCT15 (line)]] | alt | 775 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -32.7) |
| [[J82 (line)]] | alt | 796 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -26.2) |
| [[MIA PaCa-2 (line)]] | alt | 876 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -40.2) |
| [[SW480 (line)]] | alt | 789 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -32.3) |
| [[A-172 (line)]] | wt | 590 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -22.4) |
| [[A549 (line)]] | wt | 648 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -29.6) |
| [[AsPC-1 (line)]] | alt | 815 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -39.1) |
| [[Hs 766T (line)]] | wt | 918 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -27.6) |
| [[HT-29 (line)]] | alt | 752 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -31.2) |
| [[KATO III (line)]] | alt | 939 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -37.3) |
| [[LOX-IMVI (line)]] | wt | 758 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -30.7) |
| [[LS 180 (line)]] | wt | 729 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -23.6) |
| [[NCI-H1792 (line)]] | alt | 452 | 2 (2 ⚠) | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.59× (z +13.7) ⚠ cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -17.5) |
| [[Panc 03.27 (line)]] | alt | 588 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -32.7) |
| [[SNU-1 (line)]] | wt | 729 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -32.5) |
| [[SNU-423 (line)]] | alt | 1,253 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -27.5) |
| [[SW1417 (line)]] | alt | 529 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -24.7) |
| [[A-427 (line)]] | wt | 538 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -28.9) |
| [[A498 (line)]] | wt | 254 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.585× (z -12.3) |
| [[CFPAC-1 (line)]] | alt | 962 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -32.2) |
| [[CHP-212 (line)]] | wt | 484 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0963× (z -35.8) |
| [[COLO 205 (line)]] | alt | 621 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -15.6) |
| [[HepG2_C3A (line)]] | wt | 428 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -34.6) |
| [[HOP62 (line)]] | alt | 980 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -36.0) |
| [[HS-578T (line)]] | alt | 531 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -22.8) |
| [[LoVo (line)]] | wt | 546 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -23.9) |
| [[SW48 (line)]] | wt | 392 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -20.1) |
| [[NCI-H23 (line)]] | alt | 524 | 1 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.98× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -28.9) |
| [[SHP-77 (line)]] | alt | 512 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -28.4) |
| [[SK-MEL-2 (line)]] | alt | 952 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -22.5) |
| [[AN3 CA (line)]] | alt | 531 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -17.1) |
| [[SW 1271 (line)]] | alt | 463 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -23.7) |
| [[NCI-H2030 (line)]] | alt | 312 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -26.7) |
| [[NCI-H661 (line)]] | alt | 647 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -20.1) |
| [[SW 1088 (line)]] | alt | 889 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -19.7) |
| [[NCI-H2122 (line)]] | alt | 594 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 727 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2219), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENO1]] | +0.79 | +0.77 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS; STRING 996 |
| [[ALDOA]] | +0.78 | +0.76 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS; STRING 962 |
| [[LDHA]] | +0.74 | +0.78 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS; STRING 923 |
| [[SLC2A1]] | +0.71 | +0.77 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA; STRING 720 |
| [[FAM162A]] | +0.71 | +0.77 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS |
| [[INSIG2]] | +0.69 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[HK2]] | +0.69 | +0.73 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS; STRING 743 |
| [[ERO1A]] | +0.69 | +0.78 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS; STRING 439 |
| [[PKM]] | +0.68 | +0.71 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS; STRING 936 |
| [[GAPDH]] | +0.68 | +0.70 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA; STRING 999 |
| [[GPI]] | +0.67 | +0.70 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA; STRING 971 |
| [[PFKFB3]] | +0.67 | +0.63 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA; STRING 739 |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UPF3A]] | -0.65 | -0.65 / -0.60 | both halves | 7e-06 |  |
| [[ZBTB8A]] | -0.63 | -0.63 / -0.43 | both halves | 3e-05 |  |
| [[ITPA]] | -0.62 | -0.59 / -0.41 | both halves | 4e-05 |  |
| [[FAIM]] | -0.58 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[EFCAB2]] | -0.57 | -0.59 / -0.21 | both halves | 6e-04 |  |
| [[TXNRD2]] | -0.56 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[ZNF785]] | -0.56 | -0.47 / -0.32 | both halves | 2e-04 |  |
| [[UBXN2A]] | -0.55 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[GABPB1]] | -0.54 | -0.48 / -0.28 | both halves | 3e-04 |  |
| [[ZC3H7B]] | -0.54 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[HSPBAP1]] | -0.54 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[QTRT1]] | -0.54 | -0.50 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PGK1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 099]] — hypoxia; 48 genes; every member is in the + arm (projection on the module's main direction 0.837). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.1, -15.5); signed map (-37.2, 28.5). **Vector** length 143, 58.3% of its response variance represented; |z| ≥ 3 in 1,487 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Regulation of pyruvate metabolism* (reactome, mean cos +0.66 to 4); *Pyruvate metabolism* (reactome, mean cos +0.66 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +10.0 | -5.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +9.8 | -3.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +9.7 | -5.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +9.2 | +0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.9 | +3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.7 | +2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.4 | -2.1 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +3.7 | +3.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.2 | +1.0 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -10.0 | -17.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -9.5 | -10.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -9.1 | -23.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -8.4 | -14.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.6 | -41.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -4.8 | -6.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.7 | -2.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -4.1 | -4.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.5 | -1.8 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -3.4 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | phosphoglycerate kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq21.1 — chrX:77,910,739-78,129,295 (+) |
| Ensembl biotype | protein_coding |
| Hallmark sets | GLYCOLYSIS, HYPOXIA, MTORC1_SIGNALING, MYC_TARGETS_V1 |
| Reactome | 8 pathways, smallest: Gluconeogenesis; Response of Mtb to phagocytosis; Infection with Mycobacterium tuberculosis |
| Matched by | ensembl_id |

**Function**, from UniProt [P00558](https://www.uniprot.org/uniprotkb/P00558) (Phosphoglycerate kinase 1):

> Catalyzes one of the two ATP producing reactions in the glycolytic pathway via the reversible conversion of 1,3-diphosphoglycerate to 3-phosphoglycerate. Both L- and D- forms of purine and pyrimidine nucleotides can be used as substrates, but the activity is much lower on pyrimidines. In addition to its role as a glycolytic enzyme, it seems that PGK1 acts as a polymerase alpha cofactor protein (primer recognition protein). Acts as a protein kinase when localized to the mitochondrion where it …

**Summary**, from NCBI Gene [5230](https://www.ncbi.nlm.nih.gov/gene/5230):

> The protein encoded by this gene is a glycolytic enzyme that catalyzes the conversion of 1,3-diphosphoglycerate to 3-phosphoglycerate. The encoded protein may also act as a cofactor for polymerase alpha. Additionally, this protein is secreted by tumor cells where it participates in angiogenesis by functioning to reduce disulfide bonds in the serine protease, plasmin, which consequently leads to the release of the tumor blood vessel inhibitor angiostatin. The encoded protein has been identified …

**Accessions** — [HGNC:8896](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8896) · Entrez [5230](https://www.ncbi.nlm.nih.gov/gene/5230) · UniProt [P00558](https://www.uniprot.org/uniprotkb/P00558) · Ensembl [ENSG00000102144](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102144)

## Data

Gene col 2219: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2219); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2219, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2219]; `tensor/DDL_lfc|DDL_z.npy` [2219]; `embed/gene_vectors.npy` [2219]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2219 or target_col == 2219). Every well: [[PGK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PGK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
