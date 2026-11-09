---
symbol: "ASPSCR1"
type: "gene"
col: 9839
ensembl_id: "ENSG00000169696"
name: "ASPSCR1 tether for SLC2A4, UBX domain containing"
location: "17q25.3"
module: 7
arm: "+"
pooled_cpm: 20.89
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 28
n_dd_up_clean: 2
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# ASPSCR1

*ASPSCR1 tether for SLC2A4, UBX domain containing* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Ipatasertib (drug)]] 0.5 µM: 1.62× (z +6.0, q 9e-07, up in 27 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (KATO III 4.76×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (10 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.464× (z -13.5, q 7e-39, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VPS51]] (+0.55, fdr 5e-05), [[AFG3L1P]] (+0.55, fdr 1e-05), [[TPGS1]] (+0.53, fdr 2e-05); moves opposite to [[PKM]] (-0.47, fdr 3e-05), [[TMOD3]] (-0.47, fdr 5e-05), [[IL1RAP]] (-0.47, fdr 6e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9839.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (KATO III 4.76×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.62×** | +6.0 | 9e-07 | 27/46 (NCI-H460, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.29×** | +4.1 | 0.010 | 14/35 (KATO III, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Thymol (drug)]] 0.5 µM |  | **1.23×** | +3.6 | 0.066 | 14/45 (HS-578T, CFPAC-1, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.21× | +3.3 | 0.12 | 7/47 (BT-474, KATO III, …) | inconsistent across doses |  |
| [[DT-061 (drug)]] 5 µM |  | 1.43× | +3.3 | 0.12 | 3/44 (SW480, A498, …) | top dose only | noisy plate (z scaled) |
| [[Vilanterol (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.20 | 3/46 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.19× | +3.0 | 0.20 | 14/42 (HEC-1-A, HepG2/C3A, …) | inconsistent across doses | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9839.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.464×** | -13.5 | 7e-39 | 42/47 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.532×** | -11.1 | 4e-26 | 37/48 (NCI-H2030, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.556×** | -9.9 | 5e-21 | 32/46 (C32, PANC-1, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.569×** | -9.9 | 5e-21 | 36/47 (NCI-H2030, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.674×** | -9.8 | 9e-21 | 33/48 (C-33 A, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.609×** | -8.4 | 4e-15 | 31/48 (PANC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.632×** | -8.1 | 6e-14 | 34/48 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.758×** | -6.9 | 4e-10 | 31/48 (LS 180, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.775×** | -6.3 | 1e-08 | 23/48 (NCI-H2030, PANC-1, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.698×** | -6.3 | 1e-08 | 27/48 (LS 180, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.706×** | -6.1 | 5e-08 | 20/46 (LoVo, SNU-1, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.526×** | -5.9 | 2e-07 | 23/45 (A-427, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **0.709×** | -5.8 | 3e-07 | 25/44 (PANC-1, NCI-H460, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.736×** | -5.4 | 3e-06 | 23/47 (SW48, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **0.747×** | -5.1 | 1e-05 | 21/46 (NCI-H460, RPMI-7951, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.815×** | -5.1 | 1e-05 | 18/48 (Hs 766T, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.748×** | -5.1 | 1e-05 | 23/47 (Hs 766T, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.602×** | -4.7 | 9e-05 | 15/48 (A-427, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.797×** | -4.0 | 0.002 | 17/47 (MIA PaCa-2, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.811×** | -3.7 | 0.006 | 19/47 (A549, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9839. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 50.2 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -13.3) |
| [[SW480 (line)]] | alt | 57.4 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -11.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.286× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 19.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.121× (z -14.2) |
| [[PANC-1 (line)]] | alt | 29.7 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -12.0) |
| [[NCI-H23 (line)]] | alt | 26.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -12.2) |
| [[A-172 (line)]] | wt | 12.5 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.208× (z -9.4) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 24.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 22.3 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.390× (z -8.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[C-33 A (line)]] | alt | 17.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.111× (z -14.2) |
| [[C32 (line)]] | wt | 16.7 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0462× (z -16.2) |
| [[CHP-212 (line)]] | wt | 35.4 | 0 | 1 | — | [[Saquinavir (drug)]] 5 µM 0.181× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 19.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -8.6) |
| [[HS-578T (line)]] | alt | 20.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -10.1) |
| [[hTERT-HPNE (line)]] | wt | 15.4 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0912× (z -12.2) |
| [[KATO III (line)]] | alt | 17.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.76× (z +9.4) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 14.0 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.276× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 16.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.213× (z -9.3) ⚠ unreliable plate only |
| [[SK-MEL-2 (line)]] | alt | 21.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.224× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 14.7 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.135× (z -11.1) |
| [[A549 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 44.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9839), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS51]] | +0.55 | +0.40 / +0.61 | both halves | 5e-05 |  |
| [[AFG3L1P]] | +0.55 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[TPGS1]] | +0.53 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[TEN1]] | +0.53 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[L3MBTL2]] | +0.53 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[VCPKMT]] | +0.51 | +0.41 / +0.59 | both halves | 4e-05 | STRING 507 |
| [[MCRS1]] | +0.51 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[LAMTOR1]] | +0.50 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[MGRN1]] | +0.50 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[TXNRD2]] | +0.50 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[BNIP1]] | +0.50 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[TAF6L]] | +0.50 | +0.53 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PKM]] | -0.47 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[TMOD3]] | -0.47 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[IL1RAP]] | -0.47 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[GLS]] | -0.47 | -0.37 / -0.50 | both halves | 8e-05 |  |
| [[NOTCH2]] | -0.46 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[CRYBG3]] | -0.45 | -0.39 / -0.45 | both halves | 6e-05 |  |
| [[TPM3]] | -0.45 | -0.38 / -0.45 | both halves | 7e-05 |  |
| [[MYO1B]] | -0.43 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[AIDA]] | -0.43 | -0.49 / -0.36 | both halves | 9e-05 |  |
| [[EPB41L2]] | -0.43 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[TMX1]] | -0.43 | -0.49 / -0.37 | both halves | 8e-05 |  |
| [[GALNT4]] | -0.42 | -0.40 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ASPSCR1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.142). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-41.1, 11.8); signed map (-9.7, -26.9). **Vector** length 81.8, 15.9% of its response variance represented; |z| ≥ 3 in 1,031 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.6 | -1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.8 | +6.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.5 | +2.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.3 | -4.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.3 | +0.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.2 | +3.6 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.2 | +1.2 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | +1.8 | +0.4 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +1.7 | +2.6 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -8.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.4 | -6.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.0 | -9.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.1 | -8.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.0 | -5.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.0 | -1.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.0 | -3.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.0 | -2.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.8 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | ASPSCR1 tether for SLC2A4, UBX domain containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:81,976,807-82,017,406 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ASPS, ASPL, UBXD9, UBXN9, TUG |
| Gene groups (HGNC) | UBX domain containing |
| Reactome | 3 pathways, smallest: Translocation of SLC2A4 (GLUT4) to the plasma membrane; Membrane Trafficking; Vesicle-mediated transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BZE9](https://www.uniprot.org/uniprotkb/Q9BZE9) (Tether containing UBX domain for GLUT4):

> Tethering protein that sequesters GLUT4-containing vesicles in the cytoplasm in the absence of insulin. Modulates the amount of GLUT4 that is available at the cell surface (By similarity). Enhances VCP methylation catalyzed by VCPKMT.

**Summary**, from NCBI Gene [79058](https://www.ncbi.nlm.nih.gov/gene/79058):

> The protein encoded by this gene contains a UBX domain and interacts with glucose transporter type 4 (GLUT4). This protein is a tether, which sequesters the GLUT4 in intracellular vesicles in muscle and fat cells in the absence of insulin, and redistributes the GLUT4 to the plasma membrane within minutes of insulin stimulation. Translocation t(X;17)(p11;q25) of this gene with transcription factor TFE3 gene results in a ASPSCR1-TFE3 fusion protein in alveolar soft part sarcoma and in renal cell …

**Accessions** — [HGNC:13825](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13825) · Entrez [79058](https://www.ncbi.nlm.nih.gov/gene/79058) · UniProt [Q9BZE9](https://www.uniprot.org/uniprotkb/Q9BZE9) · Ensembl [ENSG00000169696](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169696)

## Data

Gene col 9839: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9839); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9839, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9839]; `tensor/DDL_lfc|DDL_z.npy` [9839]; `embed/gene_vectors.npy` [9839]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9839 or target_col == 9839). Every well: [[ASPSCR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ASPSCR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
