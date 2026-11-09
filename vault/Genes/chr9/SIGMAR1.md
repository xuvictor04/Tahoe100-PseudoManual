---
symbol: "SIGMAR1"
type: "gene"
col: 7235
ensembl_id: "ENSG00000147955"
name: "sigma receptor chaperone 1"
location: "9p13.3"
module: 20
arm: "+"
pooled_cpm: 13.22
n_lines_expressing: 48
n_dd_up: 20
n_dd_down: 4
n_dd_up_clean: 4
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# SIGMAR1

*sigma receptor chaperone 1* — 9p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (16 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 6.07× (z +16.9, q 0e+00, up in 37 of 37 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Abemaciclib (drug)]] 5 µM: 2.14× (z +3.7, q 0.008, up in 16 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.540× (z -8.1, q 2e-13, down in 31 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ICMT]] (+0.80, fdr 7e-06), [[TMEM109]] (+0.79, fdr 7e-06), [[SLC25A39]] (+0.75, fdr 7e-06); moves opposite to [[SYF2]] (-0.70, fdr 7e-06), [[MPHOSPH8]] (-0.67, fdr 7e-06), [[UBE2B]] (-0.66, fdr 7e-06).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 16 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7235.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **6.07×** | +16.9 | 0e+00 | 37/37 (SW480, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **5.03×** | +14.5 | 3e-45 | 22/23 (A498, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **3.31×** | +10.4 | 7e-23 | 26/27 (A498, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.13×** | +6.8 | 1e-09 | 28/38 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.68×** | +4.6 | 4e-04 | 24/45 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.41×** | +4.5 | 6e-04 | 22/43 (A549, HS-578T, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **1.61×** | +4.5 | 6e-04 | 20/38 (HT-29, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.60×** | +4.4 | 7e-04 | 25/45 (HOP62, hTERT-HPNE, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~52% of this change | **1.62×** | +4.3 | 9e-04 | 20/40 (NCI-H1792, A549, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **1.57×** | +4.2 | 0.001 | 24/45 (BT-474, HOP62, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~98% of this change | **1.55×** | +4.1 | 0.002 | 23/45 (HOP62, H4, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.55×** | +3.9 | 0.004 | 24/43 (HS-578T, SNU-423, …) | top dose only | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.54×** | +3.9 | 0.004 | 21/44 (NCI-H23, hTERT-HPNE, …) | top dose only | position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.32×** | +3.7 | 0.008 | 20/46 (NCI-H1792, RKO, …) | top dose only | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **2.14×** | +3.7 | 0.008 | 16/44 (AsPC-1, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.06×** | +3.5 | 0.015 | 14/44 (NCI-H460, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.023 | 14/46 (A-427, A549, …) | top dose only | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.43×** | +3.2 | 0.038 | 16/44 (NCI-H1792, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7235.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.540×** | -8.1 | 2e-13 | 31/44 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **0.546×** | -5.4 | 2e-05 | 25/44 (HepG2/C3A, AN3 CA, …) | top dose only | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.445×** | -4.0 | 0.014 | 19/42 (NCI-H23, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.622×** | -3.6 | 0.039 | 18/44 (SW480, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.68 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7235. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 20.3 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -11.1) |
| [[A498 (line)]] | wt | 28.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.63× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H460 (line)]] | wt | 11.5 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 8.69× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -9.5) |
| [[A-172 (line)]] | wt | 12.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.38× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[A549 (line)]] | wt | 10.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.63× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HEC-1-A (line)]] | alt | 19.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.46× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[Hs 766T (line)]] | wt | 17.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.23× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HS-578T (line)]] | alt | 13.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.65× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HT-29 (line)]] | alt | 9.49 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.72× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[J82 (line)]] | alt | 22.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.84× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -10.5) |
| [[KATO III (line)]] | alt | 23.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.89× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[LOX-IMVI (line)]] | wt | 12.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 8.69× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -10.2) |
| [[LS 180 (line)]] | wt | 16.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.51× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[PANC-1 (line)]] | alt | 16.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.84× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[RKO (line)]] | wt | 22.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -9.3) |
| [[SNU-423 (line)]] | alt | 7.87 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 9.81× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Menadione (drug)]] 0.05 µM 0.0719× (z -9.6) |
| [[SW480 (line)]] | alt | 18.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.87× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[C-33 A (line)]] | alt | 19.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -10.9) |
| [[HepG2_C3A (line)]] | wt | 9.56 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0816× (z -8.5) |
| [[HOP62 (line)]] | alt | 4.31 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.5 µM 0.0627× (z -10.8) |
| [[LoVo (line)]] | wt | 11.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -12.1) |
| [[MIA PaCa-2 (line)]] | alt | 10.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.19× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H1792 (line)]] | alt | 4.90 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 24.1× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H23 (line)]] | alt | 22.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -11.2) |
| [[Panc 03.27 (line)]] | alt | 13.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.48× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[RPMI-7951 (line)]] | alt | 6.40 | 0 | 1 | — | [[Acetazolamide (drug)]] 0.05 µM 0.0481× (z -9.5) |
| [[SNU-1 (line)]] | wt | 12.3 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.105× (z -8.5) |
| [[SW 900 (line)]] | alt | 5.56 | 0 | 1 | — | [[Sunitinib (drug)]] 0.05 µM 0.0626× (z -8.8) |
| [[SW48 (line)]] | wt | 18.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -9.0) |
| [[AN3 CA (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.87 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.95 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.82 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7235), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ICMT]] | +0.80 | +0.82 / +0.75 | both halves | 7e-06 |  |
| [[TMEM109]] | +0.79 | +0.75 / +0.74 | both halves | 7e-06 |  |
| [[SLC25A39]] | +0.75 | +0.82 / +0.68 | both halves | 7e-06 | STRING 494 |
| [[VMA21]] | +0.75 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[MTHFD1]] | +0.75 | +0.79 / +0.67 | both halves | 7e-06 |  |
| [[WDR77]] | +0.73 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[CDCA7]] | +0.73 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[PRKDC]] | +0.72 | +0.76 / +0.64 | both halves | 7e-06 |  |
| [[PTPN18]] | +0.71 | +0.74 / +0.54 | both halves | 1e-05 |  |
| [[PSME3]] | +0.70 | +0.72 / +0.67 | both halves | 7e-06 |  |
| [[TUBG1]] | +0.70 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[DPAGT1]] | +0.70 | +0.70 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYF2]] | -0.70 | -0.69 / -0.64 | both halves | 7e-06 |  |
| [[MPHOSPH8]] | -0.67 | -0.61 / -0.62 | both halves | 7e-06 |  |
| [[UBE2B]] | -0.66 | -0.67 / -0.69 | both halves | 7e-06 |  |
| [[TERF2IP]] | -0.66 | -0.62 / -0.62 | both halves | 7e-06 |  |
| [[NSA2]] | -0.66 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[ZMYM5]] | -0.65 | -0.66 / -0.54 | both halves | 1e-05 |  |
| [[SNHG6]] | -0.65 | -0.64 / -0.64 | both halves | 7e-06 |  |
| [[MRPL33]] | -0.65 | -0.59 / -0.69 | both halves | 7e-06 |  |
| [[CIR1]] | -0.65 | -0.65 / -0.56 | both halves | 1e-05 |  |
| [[CCDC174]] | -0.65 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[SNHG32]] | -0.64 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[NKAP]] | -0.64 | -0.66 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SIGMAR1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ALDH1B1]] | C | ALDH1B1 activity raises SIGMAR1's level | lines that do not express ALDH1B1 (3) vs lines expressing it (47) | 1.97× lower at baseline in the lines without ALDH1B1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CENPP, CDC25A, NDC80; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.651). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-29.2, -33.0); signed map (-28.1, -42.8). **Vector** length 85.0, 19.4% of its response variance represented; |z| ≥ 3 in 852 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.3 | +4.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +4.7 | +14.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +4.6 | +16.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +4.4 | +10.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~52% of this change | +3.4 | +4.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.4 | +3.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | +3.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.3 | +3.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.1 | +2.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.1 | +2.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.6 | -8.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.4 | -1.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.4 | -2.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.2 | -5.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -2.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.9 | -1.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.9 | -1.8 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -1.8 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | sigma receptor chaperone 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.3 — chr9:34,634,722-34,637,844 (-) |
| Ensembl biotype | protein_coding |
| Also known as | S1R, SIGMA1R, SR-BP1; previously OPRS1 |
| Gene groups (HGNC) | Sigma receptors |
| Hallmark sets | UV_RESPONSE_UP |
| Reactome | 3 pathways, smallest: Potential therapeutics for SARS; SARS-CoV Infections; Viral Infection Pathways |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99720](https://www.uniprot.org/uniprotkb/Q99720) (Sigma non-opioid intracellular receptor 1):

> Functions in lipid transport from the endoplasmic reticulum and is involved in a wide array of cellular functions probably through regulation of the biogenesis of lipid microdomains at the plasma membrane. Involved in the regulation of different receptors it plays a role in BDNF signaling and EGF signaling. Also regulates ion channels like the potassium channel and could modulate neurotransmitter release. Plays a role in calcium signaling through modulation together with ANK2 of the …

**Summary**, from NCBI Gene [10280](https://www.ncbi.nlm.nih.gov/gene/10280):

> This gene encodes a receptor protein that interacts with a variety of psychotomimetic drugs, including cocaine and amphetamines. The receptor is believed to play an important role in the cellular functions of various tissues associated with the endocrine, immune, and nervous systems. As indicated by its previous name, opioid receptor sigma 1 (OPRS1), the product of this gene was erroneously thought to function as an opioid receptor; it is now thought to be a non-opioid receptor. Mutations in …

**Accessions** — [HGNC:8157](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8157) · Entrez [10280](https://www.ncbi.nlm.nih.gov/gene/10280) · UniProt [Q99720](https://www.uniprot.org/uniprotkb/Q99720) · Ensembl [ENSG00000147955](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147955)

## Data

Gene col 7235: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7235); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7235, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7235]; `tensor/DDL_lfc|DDL_z.npy` [7235]; `embed/gene_vectors.npy` [7235]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7235 or target_col == 7235). Every well: [[SIGMAR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SIGMAR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
