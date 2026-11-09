---
symbol: "WT1"
type: "gene"
col: 11593
ensembl_id: "ENSG00000184937"
name: "WT1 transcription factor"
location: "11p13"
module: 110
arm: "+"
pooled_cpm: 6.83
n_lines_expressing: 21
n_dd_up: 23
n_dd_down: 20
n_dd_up_clean: 13
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 2
direction_downstream: 4
tags: ["gene", "module/110"]
generated_by: "tahoemap"
---

# WT1

*WT1 transcription factor* — 11p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.88× (z +16.0, q 0e+00, up in 8 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.551× (z -6.1, q 5e-07, down in 12 of 18 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WT1-AS]] (+0.74, fdr 7e-06, ⚠ same locus), [[LRFN5]] (+0.56, fdr 1e-05), [[FIBCD1]] (+0.54, fdr 2e-05), [[LINC01629]] (+0.53, fdr 3e-05); moves opposite to [[SWAP70]] (-0.50, fdr 3e-05), [[HS1BP3]] (-0.48, fdr 1e-04), [[UBE2H]] (-0.47, fdr 6e-05).
> It is in [[Module 110]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 4 go from it, the strongest it → [[LINC01844]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11593.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.88×** | +16.0 | 0e+00 | 8/16 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.10×** | +11.6 | 7e-29 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.18×** | +8.3 | 1e-14 | 1/12 (A549) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +5.4 | 1e-05 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.65×** | +5.2 | 3e-05 | 2/8 (SW480, MIA PaCa-2) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.61×** | +5.1 | 3e-05 | 3/12 (SW480, LS 180, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.11×** | +4.9 | 1e-04 | 2/11 (A-427, LS 180) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.35×** | +4.5 | 4e-04 | 0/8 | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +4.4 | 6e-04 | 2/17 (MIA PaCa-2, RPMI-7951) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +4.3 | 0.001 | 0/15 | top dose only | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.18×** | +4.2 | 0.002 | 1/9 (SW480) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **1.50×** | +4.1 | 0.002 | 4/17 (A549, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.9 | 0.004 | 2/17 (SW480, NCI-H23) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +3.9 | 0.004 | 2/17 (SW480, NCI-H23) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.74×** | +3.6 | 0.012 | 0/16 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Flutamide (drug)]] 5 µM |  | **1.35×** | +3.2 | 0.045 | 2/18 (LS 180, PANC-1) | top dose only |  |
| [[Darinaparsin (drug)]] 0.5 µM |  | **1.34×** | +3.1 | 0.065 | 2/18 (HepG2/C3A, HS-578T) | inconsistent across doses | position effect removed |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **1.33×** | +3.1 | 0.069 | 1/17 (SW480) | inconsistent across doses |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM |  | **1.32×** | +3.0 | 0.084 | 4/17 (A-427, J82, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.58×** | +3.0 | 0.085 | 0/15 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.58×** | +2.9 | 0.086 | 0/17 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.34×** | +2.9 | 0.096 | 0/16 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11593.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.551×** | -6.1 | 5e-07 | 12/18 (NCI-H23, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.588×** | -5.2 | 4e-05 | 6/18 (NCI-H23, PANC-1, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | **0.598×** | -5.0 | 1e-04 | 8/18 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.639×** | -4.8 | 2e-04 | 7/18 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.422×** | -4.6 | 5e-04 | 7/18 (NCI-H23, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.890× | -4.5 | 7e-04 | 4/18 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.701×** | -4.1 | 0.003 | 6/18 (SW480, PANC-1, …) | two highest doses | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.674×** | -3.9 | 0.006 | 14/18 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.684×** | -3.9 | 0.006 | 10/18 (RPMI-7951, CHP-212, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.699×** | -3.8 | 0.007 | 15/18 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.498×** | -3.7 | 0.011 | 4/18 (LS 180, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.712×** | -3.6 | 0.014 | 4/18 (COLO 205, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[AZD-8055 (drug)]] 0.05 µM |  | **0.715×** | -3.4 | 0.032 | 1/17 (A549) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.743×** | -3.2 | 0.062 | 2/18 (COLO 205, LS 180) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.746×** | -3.1 | 0.062 | 9/17 (NCI-H2030, HOP62, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.732×** | -3.1 | 0.062 | 4/18 (HOP62, J82, …) | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | **0.730×** | -3.1 | 0.062 | 1/18 (NCI-H2030) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11593. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 50.9 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.140× (z -15.4) |
| [[HOP62 (line)]] | alt | 26.0 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.136× (z -13.1) |
| [[SW480 (line)]] | alt | 11.4 | 1 | 5 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +9.3) | [[Belinostat (drug)]] 5 µM 0.0715× (z -16.5) |
| [[CHP-212 (line)]] | wt | 34.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0584× (z -9.2) |
| [[A-172 (line)]] | wt | 6.38 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0394× (z -13.5) |
| [[NCI-H23 (line)]] | alt | 17.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -16.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0575× (z -14.7) |
| [[COLO 205 (line)]] | alt | 5.26 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.05 µM 0.0407× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 11.3 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.104× (z -8.7) |
| [[J82 (line)]] | alt | 14.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -13.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 11.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0492× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[A-427 (line)]] | wt | 8.34 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.404 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.757 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.462 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.530 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.465 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.768 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.529 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.438 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.438 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.541 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.821 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.621 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.971 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.62 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.547 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.428 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.365 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.618 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.433 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.73 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.425 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.427 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.463 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.772 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.900 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.546 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.504 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.519 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11593), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WT1-AS]] | +0.74 | +0.76 / +0.66 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[LRFN5]] | +0.56 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[FIBCD1]] | +0.54 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[LINC01629]] | +0.53 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[SLC4A7]] | +0.51 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[RFWD3]] | +0.51 | +0.37 / +0.55 | both halves | 7e-05 |  |
| [[SPRED2]] | +0.50 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[ENG]] | +0.50 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[RGMB]] | +0.49 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[NHSL1]] | +0.49 | +0.33 / +0.49 | both halves | 1e-04 |  |
| [[SPRY4]] | +0.48 | +0.45 / +0.44 | both halves | 3e-05 |  |
| [[TERT]] | +0.48 | +0.36 / +0.48 | both halves | 1e-04 | STRING 526 |
| [[KCNQ5]] | +0.48 | +0.41 / +0.44 | both halves | 4e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SWAP70]] | -0.50 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[HS1BP3]] | -0.48 | -0.32 / -0.50 | both halves | 1e-04 |  |
| [[UBE2H]] | -0.47 | -0.39 / -0.52 | both halves | 6e-05 |  |
| [[OPTN]] | -0.46 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[FAM50A]] | -0.46 | -0.34 / -0.42 | both halves | 1e-04 |  |
| [[GABARAPL1]] | -0.45 | -0.36 / -0.51 | both halves | 9e-05 |  |
| [[TOM1]] | -0.44 | -0.39 / -0.36 | both halves | 1e-04 |  |
| [[CENATAC]] | -0.43 | -0.30 / -0.47 | both halves | 2e-04 |  |
| [[RHOB]] | -0.43 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[TCTA]] | -0.43 | -0.32 / -0.49 | both halves | 2e-04 |  |
| [[KIDINS220]] | -0.42 | -0.28 / -0.45 | both halves | 3e-04 |  |
| [[GABARAP]] ⚠ | -0.42 | -0.35 / -0.35 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[NEU1]] | -0.42 | -0.35 / -0.38 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises WT1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds |
| [[WT1-AS]] | C | WT1-AS activity raises WT1's level | lines that do not express WT1-AS (36) vs lines expressing it (14) | 6.02× lower at baseline in the lines without WT1-AS | 5e-05 | ⚠ within organs, on part of the lines; also absent: WT1, ZNF677, GCG; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01844]] | B | WT1 activity raises LINC01844's level | lines that do not express WT1 (29) vs lines expressing it (21) | 1.39× lower at baseline in the lines without WT1 | 0.060 | ⚠ within organs, on part of the lines; also absent: WT1-AS, INA, ZNF677 |
| [[HS1BP3]] | B | WT1 activity raises HS1BP3's level | lines that do not express WT1 (29) vs lines expressing it (21) | 1.18× lower at baseline in the lines without WT1 | 0.090 | ⚠ within organs, on part of the lines; also absent: WT1-AS, INA, ZNF677 |
| [[WT1-AS]] | C | WT1 activity raises WT1-AS's level | lines that do not express WT1 (29) vs lines expressing it (21) | 2.60× lower at baseline in the lines without WT1 | 0.005 | ⚠ within organs, on part of the lines; also absent: WT1-AS, INA, ZNF677; co-absent with the target |
| [[GLDC]] | C | WT1 activity raises GLDC's level | lines that do not express WT1 (29) vs lines expressing it (21) | 1.89× lower at baseline in the lines without WT1 | 0.055 | ⚠ within organs, on part of the lines; also absent: WT1-AS, INA, ZNF677; co-absent with the target |

## Where it sits

- **Module**: [[Module 110]]; 43 genes; every member is in the + arm (projection on the module's main direction 0.590). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (52.6, 4.8); signed map (7.4, 54.8). **Vector** length 49.7, 12.2% of its response variance represented; |z| ≥ 3 in 475 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +16.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +1.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +1.8 | +3.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.2 | +2.2 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +1.2 | +5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +3.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +0.8 | +1.9 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +0.8 | +4.1 |
|  | [[Ferulic acid (drug)]] 0.5 µM |  | +0.7 | +1.8 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +0.7 | +0.2 |
| fall | [[Trametinib (drug)]] 5 µM |  | -1.9 | -5.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.6 | -4.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.6 | -2.7 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.5 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -5.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.4 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | WT1 transcription factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p13 — chr11:32,387,775-32,435,564 (-) |
| Ensembl biotype | protein_coding |
| Also known as | WAGR, WIT-2, AWT1, NPHS4, WT-1; previously GUD |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Reactome | 12 pathways, smallest: Transcriptional regulation of testis differentiation; Nephron development; Kidney development |
| Matched by | ensembl_id |

**Function**, from UniProt [P19544](https://www.uniprot.org/uniprotkb/P19544) (Wilms tumor protein):

> Transcription factor that plays an important role in cellular development and cell survival. Recognizes and binds to the DNA sequence 5'-GCG(T/G)GGGCG-3'. Regulates the expression of numerous target genes, including EPO. Plays an essential role for development of the urogenital system. It has a tumor suppressor as well as an oncogenic role in tumor formation. Function may be isoform-specific: isoforms lacking the KTS motif may act as transcription factors. Isoforms containing the KTS motif may …

**Summary**, from NCBI Gene [7490](https://www.ncbi.nlm.nih.gov/gene/7490):

> This gene encodes a transcription factor that contains four zinc-finger motifs at the C-terminus and a proline/glutamine-rich DNA-binding domain at the N-terminus. It has an essential role in the normal development of the urogenital system, and it is mutated in a small subset of patients with Wilms tumor. This gene exhibits complex tissue-specific and polymorphic imprinting pattern, with biallelic, and monoallelic expression from the maternal and paternal alleles in different tissues. Multiple …

**Accessions** — [HGNC:12796](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12796) · Entrez [7490](https://www.ncbi.nlm.nih.gov/gene/7490) · UniProt [P19544](https://www.uniprot.org/uniprotkb/P19544) · Ensembl [ENSG00000184937](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184937)

## Data

Gene col 11593: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11593); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11593, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11593]; `tensor/DDL_lfc|DDL_z.npy` [11593]; `embed/gene_vectors.npy` [11593]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11593 or target_col == 11593). Every well: [[WT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
