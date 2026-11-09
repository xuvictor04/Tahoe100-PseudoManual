---
symbol: "TUBG2"
type: "gene"
col: 440
ensembl_id: "ENSG00000037042"
name: "tubulin gamma 2"
location: "17q21.2"
module: 83
arm: "-"
pooled_cpm: 18.99
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 12
n_dd_up_clean: 12
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# TUBG2

*tubulin gamma 2* — 17q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.09× (z +12.7, q 5e-34, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.461× (z -12.3, q 7e-32, down in 23 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.617× (z -11.7, q 5e-29, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ISCA2]] (+0.68, fdr 2e-05), [[GPATCH11]] (+0.66, fdr 1e-04), [[WRAP73]] (+0.66, fdr 3e-05); moves opposite to [[PCBP1-AS1]] (-0.69, fdr 1e-05), [[PARD6G-AS1]] (-0.68, fdr 1e-05), [[PSMD6-AS1]] (-0.67, fdr 3e-05).
> It sits in the **-** arm of [[Module 083]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[DYNC2H1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 440.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.09×** | +12.7 | 5e-34 | 40/47 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.02×** | +12.1 | 3e-31 | 39/47 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.89×** | +11.0 | 1e-25 | 41/47 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +8.0 | 3e-13 | 35/47 (LS 180, NCI-H2347, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +5.9 | 4e-07 | 23/47 (LS 180, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +5.8 | 8e-07 | 20/47 (A-427, LS 180, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.50×** | +3.7 | 0.021 | 9/47 (LS 180, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.24×** | +3.5 | 0.030 | 10/47 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.22×** | +3.4 | 0.036 | 9/47 (LS 180, CFPAC-1, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.35×** | +3.4 | 0.042 | 9/47 (PANC-1, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.32×** | +3.1 | 0.085 | 9/47 (NCI-H460, SW 900, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.41×** | +3.1 | 0.095 | 8/44 (SNU-1, A549, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 440.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.461×** | -12.3 | 7e-32 | 23/35 (HEC-1-A, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.617×** | -11.7 | 5e-29 | 36/47 (Hs 766T, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.539×** | -10.6 | 8e-24 | 34/47 (MIA PaCa-2, NCI-H661, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.667×** | -9.8 | 2e-20 | 28/46 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.577×** | -9.4 | 5e-19 | 25/41 (RPMI-7951, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.605×** | -8.1 | 5e-14 | 26/46 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.805×** | -3.7 | 0.019 | 19/47 (LOX-IMVI, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **0.817×** | -3.4 | 0.044 | 19/47 (NCI-H460, NCI-H2030, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.813×** | -3.4 | 0.044 | 16/30 (NCI-H2030, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.692×** | -3.3 | 0.058 | 7/28 (NCI-H1792, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.818×** | -3.2 | 0.068 | 2/47 (PANC-1, Panc 03.27) | inconsistent across doses | position effect removed |
| [[Berberine (chloride hydrate) (drug)]] 0.5 µM |  | **0.822×** | -3.1 | 0.080 | 8/47 (SW 1088, A-427, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 440. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 14.1 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -16.6) |
| [[MIA PaCa-2 (line)]] | alt | 25.4 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.187× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.376× (z -9.7) |
| [[HOP62 (line)]] | alt | 24.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -21.4) |
| [[hTERT-HPNE (line)]] | wt | 29.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -11.7) |
| [[RPMI-7951 (line)]] | alt | 19.3 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.112× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.104× (z -11.1) |
| [[SNU-423 (line)]] | alt | 17.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -13.1) |
| [[SW480 (line)]] | alt | 18.9 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.88× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.236× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.473× (z -9.1) |
| [[A498 (line)]] | wt | 29.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.293× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.543× (z -8.6) |
| [[J82 (line)]] | alt | 15.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -10.2) |
| [[KATO III (line)]] | alt | 20.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -11.5) |
| [[LOX-IMVI (line)]] | wt | 36.6 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.131× (z -15.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 43.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.291× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 30.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.244× (z -11.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 21.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -11.6) |
| [[SW 900 (line)]] | alt | 18.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -11.2) |
| [[A549 (line)]] | wt | 16.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -11.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 14.6 | 0 | 1 | — | [[Vandetanib (drug)]] 0.5 µM 0.194× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 13.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -10.0) |
| [[HCT15 (line)]] | alt | 27.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.176× (z -9.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 15.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.158× (z -11.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 14.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -11.8) |
| [[HT-29 (line)]] | alt | 9.55 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -8.5) |
| [[NCI-H661 (line)]] | alt | 28.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0584× (z -8.7) |
| [[PANC-1 (line)]] | alt | 15.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.345× (z -8.9) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 14.7 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0951× (z -9.1) |
| [[A-172 (line)]] | wt | 42.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.54 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.34 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.19 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.89 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 440), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 5 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ISCA2]] | +0.68 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[GPATCH11]] | +0.66 | +0.33 / +0.65 | both halves | 1e-04 |  |
| [[WRAP73]] | +0.66 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[MALSU1]] | +0.65 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[RNF114]] | +0.65 | +0.39 / +0.62 | both halves | 6e-05 |  |
| [[ZFYVE19]] | +0.64 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[TMEM276]] | +0.63 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[TRAPPC5]] | +0.63 | +0.34 / +0.60 | both halves | 1e-04 |  |
| [[TMEM256]] | +0.62 | +0.42 / +0.46 | both halves | 4e-05 |  |
| [[NDUFA12]] | +0.61 | +0.29 / +0.59 | both halves | 2e-04 |  |
| [[NFRKB]] | +0.61 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[AP2S1]] | +0.61 | +0.51 / +0.39 | both halves | 6e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCBP1-AS1]] | -0.69 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[PARD6G-AS1]] | -0.68 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[PSMD6-AS1]] | -0.67 | -0.44 / -0.64 | both halves | 3e-05 |  |
| [[SMIM15-AS1]] | -0.66 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[MPDU1]] | -0.63 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[UBE2D3-AS1]] | -0.63 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[SNAPC5]] | -0.62 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[SECISBP2]] | -0.61 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[PCBD2]] | -0.61 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[PBLD]] | -0.61 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[LINC00880]] | -0.60 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[SLC2A9]] | -0.60 | -0.52 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DYNC2H1]] | B | DYNC2H1 activity raises TUBG2's level | lines that do not express DYNC2H1 (8) vs lines expressing it (42) | 1.71× lower at baseline in the lines without DYNC2H1 | 0.044 | ⚠ within organs, on part of the lines; also absent: FJX1, GIHCG, LINC02798 |
| [[GCHFR]] | B | GCHFR activity lowers TUBG2's level | lines that do not express GCHFR (13) vs lines expressing it (37) | 1.61× higher at baseline in the lines without GCHFR | 0.045 | ⚠ within organs, on part of the lines; also absent: ARHGEF5, ATAD3C, PRKCZ; maybe low, not absent |
| [[PHC1]] | C | PHC1 activity raises TUBG2's level | lines that do not express PHC1 (4) vs lines expressing it (46) | 1.95× lower at baseline in the lines without PHC1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HECTD2, TPST1, TBKBP1; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **-** arm (projection on the module's main direction -0.713). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (7.4, 7.6); signed map (-32.7, 2.6). **Vector** length 92.8, 19.5% of its response variance represented; |z| ≥ 3 in 892 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +4.8 | +12.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.5 | +11.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.0 | +12.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.7 | +5.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +8.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.6 | +1.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.4 | +3.4 |
|  | [[Ipatasertib (drug)]] 0.05 µM |  | +1.3 | +1.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.6 | -11.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.1 | -9.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.6 | -12.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.3 | -10.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.2 | -9.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.7 | -2.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.4 | -0.2 |
|  | [[Almonertinib (hydrochloride) (drug)]] 0.05 µM |  | -1.3 | -1.3 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.3 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | tubulin gamma 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2 — chr17:42,659,284-42,667,006 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Tubulin gamma family |
| Reactome | 9 pathways, smallest: Centrosome maturation; Recruitment of mitotic centrosome proteins and complexes; Recruitment of NuMA to mitotic centrosomes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRH3](https://www.uniprot.org/uniprotkb/Q9NRH3) (Tubulin gamma-2 chain):

> Tubulin is the major constituent of microtubules, protein filaments consisting of alpha- and beta-tubulin heterodimers. Gamma-tubulin is a key component of the gamma-tubulin ring complex (gTuRC) which mediates microtubule nucleation. The gTuRC regulates the minus-end nucleation of alpha-beta tubulin heterodimers that grow into microtubule protafilaments, a critical step in centrosome duplication and spindle formation.

**Summary**, from NCBI Gene [27175](https://www.ncbi.nlm.nih.gov/gene/27175):

> Predicted to enable GTP binding activity and microtubule nucleator activity. Predicted to be involved in microtubule cytoskeleton organization and mitotic sister chromatid segregation. Located in centriolar satellite and microtubule. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:12419](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12419) · Entrez [27175](https://www.ncbi.nlm.nih.gov/gene/27175) · UniProt [Q9NRH3](https://www.uniprot.org/uniprotkb/Q9NRH3) · Ensembl [ENSG00000037042](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000037042)

## Data

Gene col 440: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 440); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 440, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 440]; `tensor/DDL_lfc|DDL_z.npy` [440]; `embed/gene_vectors.npy` [440]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 440 or target_col == 440). Every well: [[TUBG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TUBG2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
