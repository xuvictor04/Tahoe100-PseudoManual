---
symbol: "SCG5"
type: "gene"
col: 9389
ensembl_id: "ENSG00000166922"
name: "secretogranin V"
location: "15q13.3"
module: 22
arm: "+"
pooled_cpm: 17.48
n_lines_expressing: 48
n_dd_up: 20
n_dd_down: 15
n_dd_up_clean: 12
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# SCG5

*secretogranin V* — 15q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.05× (z +16.4, q 0e+00, up in 34 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.488× (z -11.6, q 2e-28, down in 29 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC18]] (+0.69, fdr 7e-06), [[MYLK2]] (+0.65, fdr 7e-06), [[GTSE1]] (+0.65, fdr 7e-06); moves opposite to [[BBS5]] (-0.51, fdr 8e-05), [[COMMD9]] (-0.51, fdr 4e-05), [[CYB5R1]] (-0.51, fdr 7e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9389.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.05×** | +16.4 | 0e+00 | 34/43 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.71×** | +12.3 | 3e-32 | 28/44 (NCI-H2030, LoVo, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +9.8 | 3e-20 | 30/44 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +8.3 | 1e-14 | 23/45 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.61×** | +7.7 | 2e-12 | 25/46 (LoVo, A549, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +6.9 | 7e-10 | 24/46 (HOP62, CFPAC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +6.7 | 2e-09 | 19/46 (PANC-1, HOP62, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.50×** | +6.6 | 4e-09 | 23/45 (HOP62, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.47×** | +6.0 | 1e-07 | 11/26 (SHP-77, SW 900, …) | inconsistent across doses | composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.40×** | +5.2 | 1e-05 | 14/45 (A549, C-33 A, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +4.9 | 6e-05 | 16/40 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.67×** | +4.3 | 7e-04 | 10/44 (PANC-1, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 1.20× | +4.2 | 0.001 | 9/46 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.30×** | +4.1 | 0.002 | 12/40 (C-33 A, SW48, …) | top dose only |  |
| [[Gefitinib (drug)]] 5 µM |  | **1.27×** | +3.9 | 0.004 | 7/46 (PANC-1, SNU-1, …) | top dose only |  |
| [[AZD1390 (drug)]] 0.05 µM |  | **1.27×** | +3.6 | 0.010 | 5/45 (Hs 766T, NCI-H1573, …) | inconsistent across doses |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.4 | 0.017 | 4/45 (RPMI-7951, HEC-1-A, …) | rises with dose | plate-row cell shift |
| [[Demeclocycline (drug)]] 5 µM |  | 1.15× | +3.2 | 0.039 | 4/46 (SW480, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9389.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.488×** | -11.6 | 2e-28 | 29/45 (HOP62, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.541×** | -9.4 | 1e-18 | 32/45 (SW 900, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.679×** | -8.9 | 1e-16 | 29/46 (SK-MEL-2, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.621×** | -7.7 | 2e-12 | 24/45 (H4, A549, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.624×** | -7.7 | 2e-12 | 21/45 (NCI-H2030, NCI-H1573, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 5 µM |  | **0.769×** | -6.0 | 2e-07 | 14/46 (RPMI-7951, SW 900, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.522×** | -5.5 | 3e-06 | 14/33 (SNU-423, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.734×** | -4.8 | 1e-04 | 17/44 (PANC-1, NCI-H1573, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.837× | -4.1 | 0.003 | 15/46 (Hs 766T, RPMI-7951, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.812×** | -3.4 | 0.041 | 10/46 (SNU-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.809×** | -3.3 | 0.043 | 11/45 (C-33 A, SNU-1, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.752×** | -3.3 | 0.043 | 10/46 (CHP-212, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.817×** | -3.3 | 0.043 | 9/45 (RPMI-7951, H4, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.821×** | -3.2 | 0.054 | 13/42 (NCI-H1573, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.822×** | -3.2 | 0.054 | 9/42 (MIA PaCa-2, Panc 03.27, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.828×** | -3.1 | 0.074 | 9/45 (HOP62, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9389. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 36.1 | 2 | 2 | [[Tucidinostat (drug)]] 5 µM 2.59× (z +10.1) | [[Ixazomib citrate (drug)]] 5 µM 0.253× (z -10.4) |
| [[SW480 (line)]] | alt | 14.0 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.80× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.161× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A-172 (line)]] | wt | 12.9 | 0 | 2 | — | [[Afatinib (drug)]] 5 µM 0.185× (z -10.9) |
| [[A-427 (line)]] | wt | 6.36 | 0 | 2 (2 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.0697× (z -10.0) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 7.43 | 0 | 2 | — | [[Riluzole hydrochloride (drug)]] 0.5 µM 0.0880× (z -9.4) |
| [[LoVo (line)]] | wt | 12.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.88× (z +12.9) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[A498 (line)]] | wt | 14.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -12.1) ⚠ cell-cycle shift, explains ~36% of this change |
| [[CFPAC-1 (line)]] | alt | 8.81 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.54× (z +8.6) | — |
| [[H4 (line)]] | wt | 27.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.130× (z -8.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HCT15 (line)]] | alt | 28.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +11.0) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[HT-29 (line)]] | alt | 5.30 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.45× (z +9.0) | — |
| [[KATO III (line)]] | alt | 9.07 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.174× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 25.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.74× (z +13.8) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[Panc 03.27 (line)]] | alt | 5.79 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.70× (z +9.1) | — |
| [[PANC-1 (line)]] | alt | 19.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +10.9) | — |
| [[RKO (line)]] | wt | 19.7 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.108× (z -9.9) |
| [[SK-MEL-2 (line)]] | alt | 15.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.217× (z -10.0) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SNU-423 (line)]] | alt | 16.0 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.157× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.58 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.99 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 56.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.17 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.62 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 75.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.99 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 18.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9389), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC18]] | +0.69 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[MYLK2]] | +0.65 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[GTSE1]] | +0.65 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[ADCY10P1]] | +0.64 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[HELLPAR]] | +0.64 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[MYH15]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[ASPM]] | +0.62 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[PAK6]] | +0.62 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[NUSAP1]] | +0.61 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[KIF2C]] | +0.60 | +0.55 / +0.68 | both halves | 1e-05 | pathway: HALLMARK_SPERMATOGENESIS |
| [[TRIM59]] | +0.60 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[CDK1]] | +0.59 | +0.60 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_SPERMATOGENESIS |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BBS5]] | -0.51 | -0.37 / -0.51 | both halves | 8e-05 |  |
| [[COMMD9]] | -0.51 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[CYB5R1]] | -0.51 | -0.37 / -0.44 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SCG5's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[AP1M2]] | B | AP1M2 activity lowers SCG5's level | lines that do not express AP1M2 (24) vs lines expressing it (26) | 1.64× higher at baseline in the lines without AP1M2 | 0.051 | ⚠ within organs, on part of the lines; also absent: CRB3, SPINT1-AS1, GRB7 |
| [[TOP1]] | B | TOP1 activity lowers SCG5's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 4.8% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.577). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-40.4, -56.0); signed map (-49.8, -46.6). **Vector** length 104, 23.8% of its response variance represented; |z| ≥ 3 in 1,112 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DREAM G2/M down* (control, mean cos +0.51 to 28); *Condensation of Prometaphase Chromosomes* (reactome, mean cos +0.52 to 8); *Kinesins* (reactome, mean cos +0.52 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +16.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +9.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +8.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.1 | +7.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +6.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.5 | +5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +6.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | +2.5 | +3.9 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -5.0 | -9.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -5.0 | -7.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.8 | -11.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -3.8 | -8.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | -7.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.3 | -4.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.7 | -4.1 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.5 | -2.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.1 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | secretogranin V |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q13.3 — chr15:32,641,676-32,697,098 (+) |
| Ensembl biotype | protein_coding |
| Also known as | 7B2, SgV; previously SGNE1 |
| Gene groups (HGNC) | Granins |
| Hallmark sets | SPERMATOGENESIS, KRAS_SIGNALING_UP |
| Matched by | ensembl_id |

**Function**, from UniProt [P05408](https://www.uniprot.org/uniprotkb/P05408) (Neuroendocrine protein 7B2):

> Acts as a molecular chaperone for PCSK2/PC2, preventing its premature activation in the regulated secretory pathway. Binds to inactive PCSK2 in the endoplasmic reticulum and facilitates its transport from there to later compartments of the secretory pathway where it is proteolytically matured and activated. Also required for cleavage of PCSK2 but does not appear to be involved in its folding. Plays a role in regulating pituitary hormone secretion. The C-terminal peptide inhibits PCSK2 in vitro. …

**Summary**, from NCBI Gene [6447](https://www.ncbi.nlm.nih.gov/gene/6447):

> This gene encodes a secreted chaperone protein that prevents the aggregation of other secreted proteins, including proteins that are associated with neurodegenerative and metabolic disease. The encoded protein may be best known for its role in the trafficking and activation of prohormone convertase PC2 (encoded by Gene ID: 5126). Phosphorylation of the encoded protein has been shown to have an inhibitory effect on its chaperone function. This gene also produces a ARHGAP11A-SCG5 readthrough …

**Accessions** — [HGNC:10816](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10816) · Entrez [6447](https://www.ncbi.nlm.nih.gov/gene/6447) · UniProt [P05408](https://www.uniprot.org/uniprotkb/P05408) · Ensembl [ENSG00000166922](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166922)

## Data

Gene col 9389: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9389); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9389, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9389]; `tensor/DDL_lfc|DDL_z.npy` [9389]; `embed/gene_vectors.npy` [9389]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9389 or target_col == 9389). Every well: [[SCG5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCG5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
