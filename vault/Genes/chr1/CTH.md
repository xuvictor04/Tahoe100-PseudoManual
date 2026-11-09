---
symbol: "CTH"
type: "gene"
col: 3836
ensembl_id: "ENSG00000116761"
name: "cystathionine gamma-lyase"
location: "1p31.1"
module: 63
arm: "+"
pooled_cpm: 26.83
n_lines_expressing: 44
n_dd_up: 17
n_dd_down: 5
n_dd_up_clean: 15
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 8
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# CTH

*cystathionine gamma-lyase* — 1p31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.78× (z +9.2, q 2e-17, up in 26 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.523× (z -7.3, q 2e-10, down in 27 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IDH1]] (+0.68, fdr 7e-06), [[MTHFD2]] (+0.63, fdr 7e-06), [[IARS1]] (+0.61, fdr 1e-05); moves opposite to [[CREB1]] (-0.52, fdr 3e-05), [[GPATCH8]] (-0.50, fdr 2e-05), [[MRM2]] (-0.47, fdr 3e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC00662]] → it (grade C ⚠); 8 go from it, the strongest it → [[PYCR1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3836.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +9.2 | 2e-17 | 26/39 (CFPAC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.30×** | +8.8 | 3e-16 | 35/40 (AsPC-1, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.00×** | +7.8 | 2e-12 | 31/41 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.74×** | +6.2 | 6e-08 | 24/42 (SW1417, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +5.5 | 3e-06 | 22/37 (NCI-H460, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.63×** | +5.5 | 3e-06 | 20/42 (A-427, LS 180, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.34×** | +5.0 | 5e-05 | 22/35 (NCI-H460, A-427, …) | all doses, flat | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.55×** | +4.9 | 6e-05 | 19/42 (SW1417, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +4.3 | 9e-04 | 18/40 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.45×** | +4.2 | 0.002 | 18/41 (SW1417, J82, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.68×** | +4.2 | 0.002 | 12/42 (MIA PaCa-2, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM |  | **1.28×** | +4.0 | 0.004 | 19/42 (SK-MEL-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.78×** | +3.4 | 0.031 | 13/40 (MIA PaCa-2, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.35×** | +3.4 | 0.031 | 15/41 (RKO, SK-MEL-2, …) | rises with dose |  |
| [[Terfenadine (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.037 | 15/42 (A498, J82, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.038 | 16/41 (SW1417, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Artesunate (drug)]] 0.5 µM |  | **1.33×** | +3.2 | 0.047 | 17/42 (SK-MEL-2, HEC-1-A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3836.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.523×** | -7.3 | 2e-10 | 27/42 (PANC-1, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.554×** | -6.7 | 8e-09 | 23/42 (KATO III, LoVo, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.871× | -5.5 | 7e-06 | 15/42 (J82, RKO, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.642×** | -4.6 | 6e-04 | 20/39 (H4, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.714×** | -3.8 | 0.016 | 17/42 (KATO III, NCI-H2347, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.741×** | -3.4 | 0.069 | 15/42 (NCI-H2347, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~6% here); position effect removed |
| [[Thymol (drug)]] 5 µM |  | 0.820× | -3.2 | 0.12 | 14/42 (HOP62, NCI-H661, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.765× | -3.0 | 0.18 | 17/42 (NCI-H2347, SW 1088, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3836. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 85.4 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -18.0) |
| [[PANC-1 (line)]] | alt | 14.9 | 0 | 6 (5 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.167× (z -12.5) |
| [[KATO III (line)]] | alt | 52.2 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.155× (z -12.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.189× (z -11.4) |
| [[NCI-H2030 (line)]] | alt | 79.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.168× (z -10.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.300× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 51.7 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.53× (z +10.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.05 µM 4.18× (z +9.0) | — |
| [[SW480 (line)]] | alt | 8.73 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.53× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.172× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[CFPAC-1 (line)]] | alt | 29.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.51× (z +14.4) | — |
| [[HCT15 (line)]] | alt | 13.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0861× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HepG2_C3A (line)]] | wt | 10.7 | 0 | 1 | — | [[Methotrexate (drug)]] 0.05 µM 0.0562× (z -10.5) |
| [[HT-29 (line)]] | alt | 27.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +9.4) | — |
| [[J82 (line)]] | alt | 11.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.66× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 6.72 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0581× (z -12.6) |
| [[NCI-H23 (line)]] | alt | 16.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -10.2) |
| [[SW1417 (line)]] | alt | 17.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +10.6) | — |
| [[A-172 (line)]] | wt | 3.63 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 68.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.14 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.65 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.74 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.87 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.90 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 59.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.30 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3836), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IDH1]] | +0.68 | +0.64 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS; STRING 405 |
| [[MTHFD2]] | +0.63 | +0.58 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 471 |
| [[IARS1]] | +0.61 | +0.56 / +0.61 | both halves | 1e-05 | pathway: Metabolism of amino acids and derivatives |
| [[GARS1]] | +0.59 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[GFPT1]] | +0.57 | +0.57 / +0.57 | both halves | 9e-06 | pathway: HALLMARK_GLYCOLYSIS; STRING 403 |
| [[PHGDH]] | +0.57 | +0.55 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 588 |
| [[SLC6A9]] | +0.56 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[CLGN]] | +0.56 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[XPOT]] | +0.55 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[AARS1]] | +0.54 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[HSPA9]] | +0.54 | +0.48 / +0.54 | both halves | 2e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[ALDH1L2]] | +0.54 | +0.50 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CREB1]] | -0.52 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[GPATCH8]] | -0.50 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[MRM2]] | -0.47 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[OBI1]] | -0.47 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[CHAMP1]] | -0.47 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[NHLRC2]] | -0.46 | -0.51 / -0.36 | both halves | 9e-05 |  |
| [[DDX52]] | -0.46 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[GGA3]] | -0.45 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[VEZF1]] | -0.45 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[CHURC1]] | -0.44 | -0.46 / -0.38 | both halves | 7e-05 |  |
| [[IL4R]] | -0.44 | -0.29 / -0.49 | both halves | 3e-04 |  |
| [[ERCC6L2]] | -0.44 | -0.51 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00662]] | C | LINC00662 activity strengthens CTH's drug response | lines that do not express LINC00662 (3) vs lines expressing it (39) | the lines without LINC00662 respond 0.83× as strongly (z diff +0.74); strongest at Panobinostat 5 µM: 0.85x vs 1.74x (z diff +3.8) | 0.083 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: NME4, ZFP14, ZNF221; target measured in part of the lines; both ways; artifact flags |
| [[LINC00662]] | C | LINC00662 activity lowers CTH's level | lines that do not express LINC00662 (3) vs lines expressing it (47) | 3.22× higher at baseline in the lines without LINC00662 | 0.085 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: NME4, ZFP14, ZNF221 |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PYCR1]] | B | CTH activity raises PYCR1's level | lines that do not express CTH (6) vs lines expressing it (44) | 1.70× lower at baseline in the lines without CTH | 0.015 | ⚠ within organs, on part of the lines; also absent: SLC35F2, POLR3G; maybe low, not absent |
| [[ATP2C1]] | B | CTH activity raises ATP2C1's level | lines that do not express CTH (6) vs lines expressing it (44) | 1.19× lower at baseline in the lines without CTH | 0.024 | ⚠ within organs, on part of the lines; also absent: SLC35F2, POLR3G; maybe low, not absent |
| [[ARG2]] | B | CTH activity raises ARG2's level | lines that do not express CTH (6) vs lines expressing it (44) | 2.46× lower at baseline in the lines without CTH | 0.025 | ⚠ within organs, on part of the lines; also absent: SLC35F2, POLR3G; maybe low, not absent |
| [[ASNS]] | B | CTH activity raises ASNS's level | lines that do not express CTH (6) vs lines expressing it (44) | 2.22× lower at baseline in the lines without CTH | 0.044 | ⚠ within organs, on part of the lines; also absent: SLC35F2, POLR3G; maybe low, not absent |
| [[SARS1]] | B | CTH activity raises SARS1's level | lines that do not express CTH (6) vs lines expressing it (44) | 1.39× lower at baseline in the lines without CTH | 0.056 | ⚠ within organs, on part of the lines; also absent: SLC35F2, POLR3G; maybe low, not absent |
| [[HYOU1]] | B | CTH activity raises HYOU1's level | lines that do not express CTH (6) vs lines expressing it (44) | 1.64× lower at baseline in the lines without CTH | 0.063 | ⚠ within organs, on part of the lines; also absent: SLC35F2, POLR3G; maybe low, not absent |
| [[GOT1]] | B | CTH activity raises GOT1's level | lines that do not express CTH (6) vs lines expressing it (44) | 1.68× lower at baseline in the lines without CTH | 0.080 | ⚠ within organs, on part of the lines; also absent: SLC35F2, POLR3G; maybe low, not absent |
| [[GARS1]] | B | CTH activity raises GARS1's level | lines that do not express CTH (6) vs lines expressing it (44) | 1.41× lower at baseline in the lines without CTH | 0.089 | ⚠ within organs, on part of the lines; also absent: SLC35F2, POLR3G; maybe low, not absent |

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.603). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.6, 47.6); signed map (-14.5, 24.9). **Vector** length 106, 26.8% of its response variance represented; |z| ≥ 3 in 997 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ISR ATF4* (control, mean cos +0.50 to 16); *unfolded protein response* (hallmark, mean cos +0.51 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +4.5 | +8.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +4.3 | +5.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.0 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.9 | +0.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | +3.7 | +1.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.9 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +5.5 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.0 | +3.3 |
|  | [[Adagrasib (drug)]] 5 µM |  | +2.0 | +1.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.9 | +0.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -6.6 | -7.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.6 | -6.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.9 | -0.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.4 | -4.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.2 | -0.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.1 | -0.0 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.1 | -3.8 |
|  | [[Belzutifan (drug)]] 5 µM |  | -1.9 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | cystathionine gamma-lyase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.1 — chr1:70,411,218-70,439,851 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CSE |
| Hallmark sets | APOPTOSIS, GLYCOLYSIS, MTORC1_SIGNALING |
| Reactome | 5 pathways, smallest: Metabolism of ingested SeMet, Sec, MeSec into H2Se; Degradation of cysteine and homocysteine; Sulfur amino acid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P32929](https://www.uniprot.org/uniprotkb/P32929) (Cystathionine gamma-lyase):

> Catalyzes the last step in the trans-sulfuration pathway from L-methionine to L-cysteine in a pyridoxal-5'-phosphate (PLP)-dependent manner, which consists on cleaving the L,L-cystathionine molecule into L-cysteine, ammonia and 2-oxobutanoate. Part of the L-cysteine derived from the trans-sulfuration pathway is utilized for biosynthesis of the ubiquitous antioxidant glutathione. Besides its role in the conversion of L-cystathionine into L-cysteine, it utilizes L-cysteine and L-homocysteine as …

**Summary**, from NCBI Gene [1491](https://www.ncbi.nlm.nih.gov/gene/1491):

> This gene encodes a cytoplasmic enzyme in the trans-sulfuration pathway that converts cystathione derived from methionine into cysteine. Glutathione synthesis in the liver is dependent upon the availability of cysteine. Mutations in this gene cause cystathioninuria. Alternative splicing of this gene results in three transcript variants encoding different isoforms. [provided by RefSeq, Jun 2010]

**Accessions** — [HGNC:2501](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2501) · Entrez [1491](https://www.ncbi.nlm.nih.gov/gene/1491) · UniProt [P32929](https://www.uniprot.org/uniprotkb/P32929) · Ensembl [ENSG00000116761](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116761)

## Data

Gene col 3836: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3836); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3836, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3836]; `tensor/DDL_lfc|DDL_z.npy` [3836]; `embed/gene_vectors.npy` [3836]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3836 or target_col == 3836). Every well: [[CTH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
