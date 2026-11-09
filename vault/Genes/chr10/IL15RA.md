---
symbol: "IL15RA"
type: "gene"
col: 5566
ensembl_id: "ENSG00000134470"
name: "interleukin 15 receptor subunit alpha"
location: "10p15.1"
module: 70
arm: "+"
pooled_cpm: 15.73
n_lines_expressing: 43
n_dd_up: 16
n_dd_down: 21
n_dd_up_clean: 12
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 22
direction_downstream: 21
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# IL15RA

*interleukin 15 receptor subunit alpha* — 10p15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 1.75× (z +8.8, q 9e-16, up in 24 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.424× (z -13.5, q 8e-39, down in 33 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APOL3]] (+0.73, fdr 7e-06), [[GBP3]] (+0.72, fdr 7e-06), [[GBP4]] (+0.71, fdr 7e-06); moves opposite to [[OSBPL8]] (-0.51, fdr 3e-04).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[RSAD2]] → it (grade B ⚠); 21 go from it, the strongest it → [[IL15]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5566.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **1.75×** | +8.8 | 9e-16 | 24/40 (PANC-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.42×** | +5.1 | 1e-04 | 17/39 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.35×** | +4.7 | 4e-04 | 16/37 (NCI-H2347, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.23×** | +4.7 | 4e-04 | 14/41 (AsPC-1, PANC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +4.5 | 9e-04 | 15/35 (AsPC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.32×** | +4.4 | 0.001 | 17/38 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +4.4 | 0.001 | 14/38 (HOP62, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.35×** | +4.3 | 0.001 | 12/39 (Hs 766T, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.58×** | +3.8 | 0.009 | 8/36 (NCI-H2347, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.009 | 12/40 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.27×** | +3.7 | 0.010 | 12/40 (HT-29, SW480, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.26×** | +3.6 | 0.013 | 7/38 (CFPAC-1, NCI-H1573, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.26×** | +3.6 | 0.013 | 13/41 (A-172, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.25×** | +3.6 | 0.014 | 12/39 (COLO 205, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Amsacrine (drug)]] 5 µM |  | 1.16× | +3.4 | 0.029 | 8/40 (A549, SK-MEL-2, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.072 | 5/39 (PANC-1, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5566.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.424×** | -13.5 | 8e-39 | 33/41 (A-172, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.448×** | -12.6 | 4e-34 | 31/41 (HEC-1-A, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.540×** | -9.0 | 5e-17 | 20/29 (A-172, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Tofacitinib (drug)]] 5 µM |  | **0.688×** | -8.3 | 1e-14 | 24/40 (CFPAC-1, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.602×** | -8.0 | 2e-13 | 24/32 (KATO III, A-172, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.702×** | -7.9 | 4e-13 | 26/39 (NCI-H1792, A498, …) | top dose only | cell-cycle shift (explains ~21% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.416×** | -7.2 | 4e-11 | 23/40 (RKO, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.657×** | -6.6 | 3e-09 | 23/40 (CFPAC-1, COLO 205, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.688×** | -5.9 | 2e-07 | 22/40 (A498, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.714×** | -5.3 | 7e-06 | 15/41 (SNU-423, LoVo, …) | inconsistent across doses | position effect removed |
| [[NG25 (drug)]] 5 µM |  | **0.536×** | -5.1 | 2e-05 | 20/38 (NCI-H1792, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.732×** | -4.9 | 5e-05 | 17/39 (A498, A-172, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.736×** | -4.4 | 5e-04 | 17/35 (SNU-423, A-172, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.596×** | -4.2 | 9e-04 | 14/36 (A-172, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **0.772×** | -4.1 | 0.002 | 13/41 (A-172, A498, …) | top dose only |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.777×** | -4.0 | 0.003 | 10/39 (NCI-H1792, A498, …) | inconsistent across doses |  |
| [[crizotinib (drug)]] 5 µM |  | **0.773×** | -3.7 | 0.006 | 11/40 (SNU-423, C-33 A, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.850× | -3.6 | 0.008 | 14/41 (CFPAC-1, LoVo, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5566. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 45.3 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -16.3) |
| [[A498 (line)]] | wt | 29.6 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -16.4) |
| [[HEC-1-A (line)]] | alt | 31.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -15.9) |
| [[LoVo (line)]] | wt | 25.2 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.236× (z -12.1) |
| [[LS 180 (line)]] | wt | 22.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.265× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 53.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -18.5) |
| [[PANC-1 (line)]] | alt | 14.9 | 1 | 2 | [[Harringtonine (drug)]] 0.5 µM 2.88× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.252× (z -11.4) |
| [[HT-29 (line)]] | alt | 18.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -13.2) |
| [[KATO III (line)]] | alt | 16.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0939× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.230× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 15.5 | 0 | 2 | — | [[Saquinavir (drug)]] 0.5 µM 0.151× (z -9.8) |
| [[SNU-423 (line)]] | alt | 21.5 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.146× (z -10.5) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.231× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 24.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +9.4) | — |
| [[Hs 766T (line)]] | wt | 22.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -8.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 13.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -9.4) |
| [[RKO (line)]] | wt | 17.6 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0263× (z -10.6) |
| [[SW1417 (line)]] | alt | 6.46 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -11.8) |
| [[SW480 (line)]] | alt | 10.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -8.7) |
| [[A-427 (line)]] | wt | 6.25 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.99 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.32 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.33 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.32 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.45 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.53 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5566), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APOL3]] | +0.73 | +0.63 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[GBP3]] | +0.72 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[GBP4]] | +0.71 | +0.60 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[LINC02100]] | +0.70 | +0.59 / +0.74 | both halves | 7e-06 |  |
| [[APOL6]] | +0.70 | +0.55 / +0.72 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[CD5L]] | +0.69 | +0.67 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[PARP12]] | +0.69 | +0.63 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[CASP7]] | +0.67 | +0.58 / +0.63 | both halves | 8e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[APOL2]] | +0.66 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[PSMB10]] | +0.66 | +0.47 / +0.66 | both halves | 2e-05 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[TAP2]] | +0.66 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[PSMB9]] | +0.66 | +0.52 / +0.69 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OSBPL8]] | -0.51 | -0.28 / -0.51 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 21, C 1. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RSAD2]] | B | RSAD2 activity raises IL15RA's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 1.86× lower at baseline in the lines without RSAD2 | 0.012 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[PLAAT4]] | B | PLAAT4 activity raises IL15RA's level | lines that do not express PLAAT4 (21) vs lines expressing it (29) | 2.38× lower at baseline in the lines without PLAAT4 | 0.018 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1 |
| [[APOL1]] | B | APOL1 activity raises IL15RA's level | lines that do not express APOL1 (24) vs lines expressing it (26) | 1.95× lower at baseline in the lines without APOL1 | 0.024 | ⚠ within organs, on part of the lines; also absent: POU5F1, UGT1A6, NMRAL2P-1 |
| [[GBP3]] | B | GBP3 activity raises IL15RA's level | lines that do not express GBP3 (11) vs lines expressing it (39) | 2.55× lower at baseline in the lines without GBP3 | 0.031 | ⚠ within organs, on part of the lines; also absent: PHLDA2, CD44, ITGA3 |
| [[TNFSF10]] | B | TNFSF10 activity raises IL15RA's level | lines that do not express TNFSF10 (24) vs lines expressing it (26) | 2.28× lower at baseline in the lines without TNFSF10 | 0.032 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TMEM92, LY75 |
| [[IL15]] | B | IL15 activity raises IL15RA's level | lines that do not express IL15 (10) vs lines expressing it (40) | 2.05× lower at baseline in the lines without IL15 | 0.033 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent |
| [[GBP4]] | B | GBP4 activity raises IL15RA's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 1.61× lower at baseline in the lines without GBP4 | 0.034 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[EPSTI1]] | B | EPSTI1 activity raises IL15RA's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 1.70× lower at baseline in the lines without EPSTI1 | 0.042 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |
| [[LYN]] | B | LYN activity raises IL15RA's level | lines that do not express LYN (8) vs lines expressing it (42) | 2.40× lower at baseline in the lines without LYN | 0.046 | ⚠ within organs, on part of the lines; also absent: SLC12A7, NGEF, ENSG00000289862; maybe low, not absent |
| [[IFI16]] | B | IFI16 activity raises IL15RA's level | lines that do not express IFI16 (18) vs lines expressing it (32) | 1.42× lower at baseline in the lines without IFI16 | 0.049 | ⚠ within organs, on part of the lines; also absent: MMP14, IL1A, MAF |
| [[GBP1]] | B | GBP1 activity raises IL15RA's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 1.66× lower at baseline in the lines without GBP1 | 0.051 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[JAK2]] | B | JAK2 activity raises IL15RA's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 4.2% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 21, C 0. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL15]] | B | IL15RA activity raises IL15's level | lines that do not express IL15RA (7) vs lines expressing it (43) | 3.08× lower at baseline in the lines without IL15RA | 0.011 | ⚠ within organs, on part of the lines; also absent: CLCF1, SGMS2 |
| [[LYN]] | B | IL15RA activity raises LYN's level | lines that do not express IL15RA (7) vs lines expressing it (43) | 3.66× lower at baseline in the lines without IL15RA | 0.011 | ⚠ within organs, on part of the lines; also absent: CLCF1, SGMS2 |
| [[PSMB10]] | B | IL15RA activity raises PSMB10's level | lines that do not express IL15RA (7) vs lines expressing it (43) | 1.84× lower at baseline in the lines without IL15RA | 0.016 | ⚠ within organs, on part of the lines; also absent: CLCF1, SGMS2 |
| [[NMI]] | B | IL15RA activity raises NMI's level | lines that do not express IL15RA (7) vs lines expressing it (43) | 2.42× lower at baseline in the lines without IL15RA | 0.025 | ⚠ within organs, on part of the lines; also absent: CLCF1, SGMS2 |
| [[BID]] | B | IL15RA activity raises BID's level | lines that do not express IL15RA (7) vs lines expressing it (43) | 1.95× lower at baseline in the lines without IL15RA | 0.034 | ⚠ within organs, on part of the lines; also absent: CLCF1, SGMS2 |
| [[TRIM5]] | B | IL15RA activity raises TRIM5's level | lines that do not express IL15RA (7) vs lines expressing it (43) | 2.19× lower at baseline in the lines without IL15RA | 0.039 | ⚠ within organs, on part of the lines; also absent: CLCF1, SGMS2 |
| [[ERAP2]] | B | IL15RA activity raises ERAP2's level | lines that do not express IL15RA (7) vs lines expressing it (43) | 1.79× lower at baseline in the lines without IL15RA | 0.042 | ⚠ within organs, on part of the lines; also absent: CLCF1, SGMS2 |
| [[HLA-F]] | B | IL15RA activity raises HLA-F's level | lines that do not express IL15RA (7) vs lines expressing it (43) | 3.32× lower at baseline in the lines without IL15RA | 0.043 | ⚠ within organs, on part of the lines; also absent: CLCF1, SGMS2 |
| [[NEURL3]] | B | IL15RA activity raises NEURL3's level | lines that do not express IL15RA (7) vs lines expressing it (43) | 1.86× lower at baseline in the lines without IL15RA | 0.044 | ⚠ within organs, on part of the lines; also absent: CLCF1, SGMS2 |
| [[RBM43]] | B | IL15RA activity raises RBM43's level | lines that do not express IL15RA (7) vs lines expressing it (43) | 1.84× lower at baseline in the lines without IL15RA | 0.051 | ⚠ within organs, on part of the lines; also absent: CLCF1, SGMS2 |
| [[GBP1]] | B | IL15RA activity raises GBP1's level | lines that do not express IL15RA (7) vs lines expressing it (43) | 2.05× lower at baseline in the lines without IL15RA | 0.060 | ⚠ within organs, on part of the lines; also absent: CLCF1, SGMS2 |
| [[NLRC5]] | B | IL15RA activity raises NLRC5's level | lines that do not express IL15RA (7) vs lines expressing it (43) | 2.16× lower at baseline in the lines without IL15RA | 0.060 | ⚠ within organs, on part of the lines; also absent: CLCF1, SGMS2 |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.700). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (44.8, 52.7); signed map (61.0, 30.8). **Vector** length 105, 26.2% of its response variance represented; |z| ≥ 3 in 912 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Non-canonical inflammasome activation* (reactome, mean cos +0.58 to 4); *Antigen processing: Ub, ATP-independent proteasomal degradation* (reactome, mean cos +0.59 to 4); *CASP4 inflammasome assembly* (reactome, mean cos +0.59 to 3).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +5.2 | +8.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +3.9 | +3.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | +3.9 | +3.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +3.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.6 | +4.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.3 | +5.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.5 | +4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | -0.7 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.7 | -8.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | -4.2 | -3.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.2 | -5.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.1 | -12.6 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -4.0 | -8.3 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -3.4 | -6.6 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -3.2 | -4.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.2 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | interleukin 15 receptor subunit alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p15.1 — chr10:5,943,639-5,978,187 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CD215, IL-15RA |
| Gene groups (HGNC) | CD molecules; Interleukin receptors; Sushi domain containing |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, INFLAMMATORY_RESPONSE, INTERFERON_GAMMA_RESPONSE, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 4 pathways, smallest: Interleukin-15 signaling; Interleukin-2 family signaling; Signaling by Interleukins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13261](https://www.uniprot.org/uniprotkb/Q13261) (Interleukin-15 receptor subunit alpha):

> High-affinity receptor for interleukin-15. Can signal both in cis and trans where IL15R from one subset of cells presents IL15 to neighboring IL2RG-expressing cells (By similarity). In neutrophils, binds and activates kinase SYK in response to IL15 stimulation. In neutrophils, required for IL15-induced phagocytosis in a SYK-dependent manner. Expression of different isoforms may alter or interfere with signal transduction.; [Isoform 5]: Does not bind IL15.; [Isoform 6]: Does not bind IL15.; …

**Summary**, from NCBI Gene [3601](https://www.ncbi.nlm.nih.gov/gene/3601):

> This gene encodes a cytokine receptor that specifically binds interleukin 15 (IL15) with high affinity. The receptors of IL15 and IL2 share two subunits, IL2R beta and IL2R gamma. This forms the basis of many overlapping biological activities of IL15 and IL2. The protein encoded by this gene is structurally related to IL2R alpha, an additional IL2-specific alpha subunit necessary for high affinity IL2 binding. Unlike IL2RA, IL15RA is capable of binding IL15 with high affinity independent of …

**Accessions** — [HGNC:5978](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5978) · Entrez [3601](https://www.ncbi.nlm.nih.gov/gene/3601) · UniProt [Q13261](https://www.uniprot.org/uniprotkb/Q13261) · Ensembl [ENSG00000134470](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134470)

## Data

Gene col 5566: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5566); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5566, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5566]; `tensor/DDL_lfc|DDL_z.npy` [5566]; `embed/gene_vectors.npy` [5566]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5566 or target_col == 5566). Every well: [[IL15RA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IL15RA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
