---
symbol: "TSEN15"
type: "gene"
col: 12712
ensembl_id: "ENSG00000198860"
name: "tRNA splicing endonuclease subunit 15"
location: "1q25.3"
module: 63
arm: "+"
pooled_cpm: 25.38
n_lines_expressing: 50
n_dd_up: 42
n_dd_down: 5
n_dd_up_clean: 32
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# TSEN15

*tRNA splicing endonuclease subunit 15* — 1q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (10 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.71× (z +15.5, q 0e+00, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.778× (z -5.5, q 2e-05, down in 23 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZFAND1]] (+0.62, fdr 1e-05), [[TNPO1]] (+0.62, fdr 1e-05), [[IDE]] (+0.62, fdr 7e-06); moves opposite to [[AVIL]] (-0.54, fdr 2e-05), [[DALRD3]] (-0.53, fdr 3e-05), [[IFT140]] (-0.52, fdr 2e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PIR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12712.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.71×** | +15.5 | 0e+00 | 44/47 (MIA PaCa-2, A498, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.82×** | +9.3 | 3e-18 | 42/48 (NCI-H460, C-33 A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +8.9 | 1e-16 | 24/35 (MIA PaCa-2, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.76×** | +8.8 | 2e-16 | 37/47 (COLO 205, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.75×** | +8.7 | 3e-16 | 33/48 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.72×** | +8.5 | 2e-15 | 30/43 (A549, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +7.1 | 1e-10 | 25/47 (A-427, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.55×** | +6.8 | 7e-10 | 29/47 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.58×** | +6.7 | 2e-09 | 27/48 (A498, LoVo, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +6.4 | 9e-09 | 24/48 (LOX-IMVI, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.51×** | +6.4 | 9e-09 | 30/47 (COLO 205, SNU-423, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.55×** | +6.3 | 2e-08 | 22/39 (A-172, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.50×** | +6.3 | 2e-08 | 27/47 (HOP62, A498, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.13×** | +6.1 | 4e-08 | 22/40 (LoVo, SW1417, …) | all doses, flat | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.46×** | +5.9 | 2e-07 | 24/47 (NCI-H460, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.40×** | +5.3 | 5e-06 | 23/48 (COLO 205, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.40×** | +5.2 | 7e-06 | 22/47 (A498, HOP62, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.89×** | +5.2 | 7e-06 | 23/48 (RKO, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.39×** | +5.1 | 1e-05 | 22/47 (A-427, MIA PaCa-2, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.37×** | +4.9 | 3e-05 | 22/47 (A-172, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.22×** | +4.3 | 4e-04 | 16/48 (A498, NCI-H2030, …) | two highest doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.30×** | +4.1 | 9e-04 | 17/47 (NCI-H1573, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12712.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.778×** | -5.5 | 2e-05 | 23/47 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.537×** | -5.0 | 1e-04 | 22/46 (PANC-1, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM |  | **0.763×** | -4.2 | 0.005 | 18/48 (PANC-1, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.641×** | -3.6 | 0.044 | 22/46 (SNU-1, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.852× | -3.5 | 0.053 | 16/48 (SW1417, NCI-H2347, …) | top dose only |  |
| [[4EGI-1 (drug)]] 5 µM |  | **0.659×** | -3.4 | 0.067 | 16/45 (HOP62, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | 0.676× | -3.2 | 0.12 | 7/48 (A498, HS-578T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.811× | -3.1 | 0.15 | 14/47 (SW48, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12712. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 38.2 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -14.4) |
| [[PANC-1 (line)]] | alt | 39.4 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.321× (z -13.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 33.8 | 1 | 1 | [[Auranofin (drug)]] 5 µM 3.77× (z +13.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -9.0) |
| [[LoVo (line)]] | wt | 25.3 | 1 | 1 | [[Auranofin (drug)]] 5 µM 4.72× (z +11.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 15.0 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 14.4× (z +14.1) | — |
| [[SHP-77 (line)]] | alt | 32.9 | 0 | 2 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.203× (z -10.8) |
| [[SW48 (line)]] | wt | 32.3 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 5.70× (z +9.5) | [[Digitoxin (drug)]] 5 µM 0.210× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 27.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.35× (z +11.6) | — |
| [[A549 (line)]] | wt | 19.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +8.8) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 18.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 9.28× (z +12.3) | — |
| [[HCT15 (line)]] | alt | 16.0 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0903× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 21.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.74× (z +8.6) | — |
| [[HOP62 (line)]] | alt | 12.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.58× (z +10.8) | — |
| [[HT-29 (line)]] | alt | 26.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.262× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 11.9 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.0963× (z -9.2) |
| [[KATO III (line)]] | alt | 24.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.31× (z +8.5) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 16.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.13× (z +8.6) | — |
| [[LS 180 (line)]] | wt | 29.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.01× (z +10.1) | — |
| [[NCI-H1573 (line)]] | alt | 29.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -11.0) |
| [[RKO (line)]] | wt | 20.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.95× (z +10.1) | — |
| [[SK-MEL-2 (line)]] | alt | 30.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.44× (z +9.1) | — |
| [[SNU-1 (line)]] | wt | 39.1 | 0 | 1 | — | [[PF-06260933 (drug)]] 5 µM 0.0576× (z -8.6) |
| [[SNU-423 (line)]] | alt | 8.61 | 1 | 0 | [[Auranofin (drug)]] 5 µM 8.61× (z +8.8) | — |
| [[SW480 (line)]] | alt | 50.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -9.8) |
| [[A-427 (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12712), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFAND1]] | +0.62 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[TNPO1]] | +0.62 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[IDE]] | +0.62 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[VPS36]] | +0.62 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[PROSER1]] | +0.61 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[CEBPG]] | +0.60 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[PSAT1]] | +0.59 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[XPOT]] | +0.59 | +0.51 / +0.57 | both halves | 1e-05 | pathway: tRNA processing |
| [[APIP]] | +0.59 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[DTWD2]] | +0.59 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[PPA2]] | +0.58 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[TCEA1]] | +0.58 | +0.45 / +0.57 | both halves | 3e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AVIL]] | -0.54 | -0.46 / -0.56 | both halves | 2e-05 |  |
| [[DALRD3]] | -0.53 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[IFT140]] | -0.52 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[UBAP2]] | -0.52 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[ZNF324]] | -0.52 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[CXCR4]] | -0.52 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[RSPRY1]] | -0.51 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[IQCD]] | -0.50 | -0.29 / -0.42 | both halves | 2e-04 |  |
| [[TPRN]] | -0.50 | -0.26 / -0.50 | both halves | 3e-04 |  |
| [[TOB2]] | -0.49 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[INTS6L]] | -0.49 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[AAMDC]] | -0.49 | -0.46 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIR]] | B | PIR activity raises TSEN15's level | lines that do not express PIR (10) vs lines expressing it (40) | 1.55× lower at baseline in the lines without PIR | 0.040 | ⚠ within organs, on part of the lines; also absent: VEGFD, ELMO1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.516). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-28.6, -15.0); signed map (-11.3, -41.0). **Vector** length 120, 32.8% of its response variance represented; |z| ≥ 3 in 1,012 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Serine metabolism* (reactome, mean cos +0.52 to 3).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.3 | +15.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +7.0 | +9.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +4.7 | +4.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.5 | +6.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.5 | +6.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.8 | +3.6 |
|  | [[Neratinib (drug)]] 5 µM |  | +3.7 | +4.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.6 | -5.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | +0.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -0.5 |
|  | [[Selinexor (drug)]] 0.05 µM |  | -3.5 | -4.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.1 | +3.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.0 | -3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.0 | -5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -3.5 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -2.2 | -2.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.2 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | tRNA splicing endonuclease subunit 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.3 — chr1:184,051,651-184,123,978 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C1orf19 |
| Gene groups (HGNC) | tRNA-splicing endonuclease subunits |
| Reactome | 3 pathways, smallest: tRNA processing in the nucleus; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WW01](https://www.uniprot.org/uniprotkb/Q8WW01) (tRNA-splicing endonuclease subunit Sen15):

> Non-catalytic subunit of the tRNA-splicing endonuclease complex, a complex responsible for identification and cleavage of the splice sites in pre-tRNA. It cleaves pre-tRNA at the 5' and 3' splice sites to release the intron. The products are an intron and two tRNA half-molecules bearing 2',3' cyclic phosphate and 5'-OH termini. There are no conserved sequences at the splice sites, but the intron is invariably located at the same site in the gene, placing the splice sites an invariant distance …

**Summary**, from NCBI Gene [116461](https://www.ncbi.nlm.nih.gov/gene/116461):

> This gene encodes a subunit of the tRNA splicing endonuclease, which catalyzes the removal of introns from tRNA precursors. Alternative splicing results in multiple transcript variants. There is a pseudogene of this gene on chromosome 17. [provided by RefSeq, Jul 2014]

**Accessions** — [HGNC:16791](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16791) · Entrez [116461](https://www.ncbi.nlm.nih.gov/gene/116461) · UniProt [Q8WW01](https://www.uniprot.org/uniprotkb/Q8WW01) · Ensembl [ENSG00000198860](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198860)

## Data

Gene col 12712: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12712); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12712, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12712]; `tensor/DDL_lfc|DDL_z.npy` [12712]; `embed/gene_vectors.npy` [12712]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12712 or target_col == 12712). Every well: [[TSEN15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSEN15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
