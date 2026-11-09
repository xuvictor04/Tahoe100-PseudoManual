---
symbol: "POLDIP2"
type: "gene"
col: 42
ensembl_id: "ENSG00000004142"
name: "DNA polymerase delta interacting protein 2"
location: "17q11.2"
module: 148
arm: "+"
pooled_cpm: 24.14
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 5
n_dd_up_clean: 5
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/148"]
generated_by: "tahoemap"
---

# POLDIP2

*DNA polymerase delta interacting protein 2* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.78× (z +16.3, q 0e+00, up in 39 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.74× (z +12.4, q 4e-33, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Irinotecan (hydrochloride) (drug)]] 0.5 µM: 0.723× (z -5.2, q 1e-04, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C8orf33]] (+0.72, fdr 7e-06), [[MAPKAPK5]] (+0.70, fdr 1e-05), [[ADAT1]] (+0.67, fdr 1e-05); moves opposite to [[RPL18]] (-0.58, fdr 3e-05, ⚠ RPL18 in the vector space only through flagged drug-doses), [[HMGN3]] (-0.58, fdr 3e-05), [[TOMM7]] (-0.58, fdr 7e-05), [[GUSBP18]] (-0.57, fdr 2e-04).
> It sits in the **+** arm of [[Module 148]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Bendamustine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 10 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 42.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.78×** | +16.3 | 0e+00 | 39/42 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.74×** | +15.4 | 0e+00 | 34/35 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +12.4 | 4e-33 | 43/47 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.13×** | +11.1 | 1e-26 | 33/39 (MIA PaCa-2, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.55×** | +7.0 | 4e-10 | 29/45 (BT-474, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +5.8 | 7e-07 | 32/48 (RKO, NCI-H23, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.39×** | +5.0 | 4e-05 | 23/48 (MIA PaCa-2, SNU-423, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.38×** | +5.0 | 5e-05 | 24/46 (NCI-H460, NCI-H2030, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +4.9 | 7e-05 | 22/43 (MIA PaCa-2, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.33×** | +4.6 | 3e-04 | 20/47 (COLO 205, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.32×** | +4.3 | 9e-04 | 20/48 (SW480, NCI-H460, …) | rises with dose | composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +4.1 | 0.002 | 19/47 (SW480, HCT15, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.9 | 0.004 | 18/48 (NCI-H2347, C32, …) | top dose only | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.27×** | +3.8 | 0.006 | 18/48 (SW480, NCI-H460, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.24×** | +3.4 | 0.029 | 13/47 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 42.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.723×** | -5.2 | 1e-04 | 28/48 (SW480, LoVo, …) | two highest doses | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.812×** | -4.7 | 7e-04 | 25/48 (CHP-212, SW48, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.760×** | -4.4 | 0.002 | 23/48 (J82, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.761×** | -4.4 | 0.002 | 19/47 (LS 180, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.786×** | -3.8 | 0.014 | 15/47 (HS-578T, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tadalafil (drug)]] 5 µM |  | 0.810× | -3.2 | 0.12 | 15/47 (LS 180, SNU-423, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.696× | -3.0 | 0.20 | 7/47 (A-427, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 42. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 38.7 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +10.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 26.6 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.54× (z +12.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +8.5) | — |
| [[A498 (line)]] | wt | 39.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +12.2) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 27.2 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.99× (z +12.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +9.7) | — |
| [[J82 (line)]] | alt | 27.8 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.65× (z +10.8) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 5 µM 0.359× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 21.6 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +10.3) | — |
| [[NCI-H460 (line)]] | wt | 23.0 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.23× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +12.0) | — |
| [[A-427 (line)]] | wt | 29.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -15.8) ⚠ cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 19.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.14× (z +11.1) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 20.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.13× (z +9.0) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 31.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +12.3) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 24.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.69× (z +13.3) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 12.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.27× (z +10.0) | — |
| [[HEC-1-A (line)]] | alt | 33.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.60× (z +11.6) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 15.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.83× (z +9.8) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 17.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0664× (z -13.3) ⚠ toxic; cell-cycle shift, explains ~53% of this change |
| [[LOX-IMVI (line)]] | wt | 22.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.06× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 40.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +9.3) | — |
| [[NCI-H23 (line)]] | alt | 29.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.230× (z -10.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 28.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.93× (z +8.8) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 19.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.74× (z +10.2) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 42), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C8orf33]] | +0.72 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[MAPKAPK5]] | +0.70 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[ADAT1]] | +0.67 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[VPS52]] | +0.66 | +0.59 / +0.57 | both halves | 8e-06 |  |
| [[PSME3IP1]] | +0.65 | +0.65 / +0.46 | both halves | 2e-05 |  |
| [[RNASEH1]] | +0.64 | +0.68 / +0.45 | both halves | 3e-05 |  |
| [[OTUB1]] | +0.63 | +0.45 / +0.66 | both halves | 3e-05 |  |
| [[PEF1]] | +0.63 | +0.67 / +0.44 | both halves | 3e-05 |  |
| [[KARS1]] | +0.62 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[PIGW]] | +0.62 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[WDR74]] | +0.61 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[MRPL30]] | +0.60 | +0.58 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 6 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL18]] ⚠ | -0.58 | -0.46 / -0.49 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[HMGN3]] | -0.58 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[TOMM7]] | -0.58 | -0.59 / -0.38 | both halves | 7e-05 |  |
| [[GUSBP18]] | -0.57 | -0.55 / -0.29 | both halves | 2e-04 |  |
| [[RPS3]] ⚠ | -0.57 | -0.44 / -0.49 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CFD]] | -0.56 | -0.40 / -0.42 | both halves | 4e-05 |  |
| [[RPL37A]] ⚠ | -0.56 | -0.47 / -0.48 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SLC25A5]] | -0.54 | -0.36 / -0.39 | both halves | 9e-05 |  |
| [[TNNI3]] | -0.54 | -0.47 / -0.38 | both halves | 7e-05 |  |
| [[RPL35A]] | -0.54 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[C4orf48]] | -0.54 | -0.53 / -0.27 | both halves | 3e-04 |  |
| [[RPL36]] | -0.53 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[RPLP1]] | -0.53 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[COX7C]] | -0.53 | -0.57 / -0.34 | both halves | 1e-04 |  |
| [[COX6A1]] | -0.53 | -0.55 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers POLDIP2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Bendamustine (drug)]] 0.5 µM | C | POLDIP2's natural level lowers the cells' numbers under Bendamustine 0.5 µM (makes them more sensitive) | POLDIP2's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.58 | 0.491 over the table, 0.087 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 148]]; 30 genes; this gene is in the **+** arm (projection on the module's main direction 0.753). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-10.7, 7.2); signed map (15.0, -26.0). **Vector** length 63.4, 11.1% of its response variance represented; |z| ≥ 3 in 767 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +12.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.1 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +5.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +2.8 | +5.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.8 | +2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +1.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.5 | -0.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.4 | +2.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.4 | +1.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.5 | -4.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | -2.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.4 | -2.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.0 | -2.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | -1.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.4 | -2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.3 | -1.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | DNA polymerase delta interacting protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:28,346,633-28,357,527 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PDIP38, DKFZP586F1524 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2S7](https://www.uniprot.org/uniprotkb/Q9Y2S7) (Polymerase delta-interacting protein 2):

> Involved in DNA damage tolerance by regulating translesion synthesis (TLS) of templates carrying DNA damage lesions such as 8oxoG and abasic sites. May act by stimulating activity of DNA polymerases involved in TLS, such as PRIMPOL and polymerase delta (POLD1).

**Summary**, from NCBI Gene [26073](https://www.ncbi.nlm.nih.gov/gene/26073):

> This gene encodes a protein that interacts with the DNA polymerase delta p50 subunit, as well as with proliferating cell nuclear antigen. The encoded protein maybe play a role in the ability of the replication fork to bypass DNA lesions. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Feb 2014]

**Accessions** — [HGNC:23781](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23781) · Entrez [26073](https://www.ncbi.nlm.nih.gov/gene/26073) · UniProt [Q9Y2S7](https://www.uniprot.org/uniprotkb/Q9Y2S7) · Ensembl [ENSG00000004142](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000004142)

## Data

Gene col 42: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 42); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 42, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 42]; `tensor/DDL_lfc|DDL_z.npy` [42]; `embed/gene_vectors.npy` [42]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 42 or target_col == 42). Every well: [[POLDIP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLDIP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
