---
symbol: "ARHGEF37"
type: "gene"
col: 11371
ensembl_id: "ENSG00000183111"
name: "Rho guanine nucleotide exchange factor 37"
location: "5q32"
module: 10
arm: "+"
pooled_cpm: 9.49
n_lines_expressing: 46
n_dd_up: 32
n_dd_down: 11
n_dd_up_clean: 24
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# ARHGEF37

*Rho guanine nucleotide exchange factor 37* — 5q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.65× (z +26.0, q 0e+00, up in 37 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.500× (z -9.9, q 3e-20, down in 28 of 42 measured lines).
> Its strongest partners by |cos| (56 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 44 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM202-AS1]] (+0.70, fdr 1e-04), [[F8]] (+0.69, fdr 1e-04), [[SEPTIN7-DT]] (+0.68, fdr 2e-04); moves opposite to [[GNA12]] (-0.62, fdr 0.001, ⚠ one half only (not replicated)), [[PCMT1]] (-0.60, fdr 0.002, ⚠ one half only (not replicated)), [[LPCAT4]] (-0.59, fdr 0.001, ⚠ one half only (not replicated)), [[SNRPD2]] (-0.59, fdr 5e-04), [[MYPOP]] (-0.58, fdr 5e-04), [[GTF2E2]] (-0.58, fdr 5e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[ACAA2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11371.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.65×** | +26.0 | 0e+00 | 37/39 (HOP62, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.33×** | +24.2 | 0e+00 | 31/36 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.05×** | +14.6 | 0e+00 | 19/23 (SW480, HOP62, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.37×** | +12.2 | 3e-32 | 17/30 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.34×** | +12.1 | 2e-31 | 23/36 (LoVo, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.93×** | +9.0 | 2e-17 | 7/18 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.45×** | +7.5 | 7e-12 | 15/42 (HOP62, SW1417, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.59×** | +6.6 | 4e-09 | 17/42 (HOP62, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.55×** | +6.2 | 4e-08 | 20/43 (PANC-1, KATO III, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.48×** | +5.5 | 2e-06 | 12/39 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.48×** | +5.5 | 2e-06 | 16/40 (HOP62, A-427, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +5.4 | 2e-06 | 12/36 (HOP62, LS 180, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +5.2 | 8e-06 | 12/33 (SW1417, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.29×** | +5.2 | 1e-05 | 13/41 (KATO III, A-427, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +5.1 | 2e-05 | 12/41 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.41×** | +4.9 | 4e-05 | 11/40 (KATO III, NCI-H1792, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.38×** | +4.6 | 2e-04 | 14/40 (MIA PaCa-2, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.31×** | +4.0 | 0.002 | 8/44 (MIA PaCa-2, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.32×** | +3.9 | 0.003 | 7/43 (SW48, LoVo, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.32×** | +3.8 | 0.004 | 11/41 (LoVo, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11371.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.500×** | -9.9 | 3e-20 | 28/42 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.578×** | -7.8 | 2e-12 | 25/41 (LoVo, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.586×** | -7.6 | 5e-12 | 25/41 (LS 180, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.592×** | -7.5 | 1e-11 | 23/37 (NCI-H23, AN3 CA, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.606×** | -7.1 | 1e-10 | 20/41 (NCI-H460, SW48, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.704×** | -4.8 | 1e-04 | 18/35 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.718×** | -4.7 | 2e-04 | 14/42 (A-427, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.738×** | -4.3 | 0.001 | 17/42 (AN3 CA, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.782×** | -3.3 | 0.055 | 11/40 (NCI-H1573, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.648×** | -3.2 | 0.069 | 14/37 (Hs 766T, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.651×** | -3.2 | 0.070 | 8/39 (HEC-1-A, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11371. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 6.71 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.59× (z +13.9) | — |
| [[NCI-H2030 (line)]] | alt | 7.08 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +10.5) | [[Simotinib (drug)]] 5 µM 0.117× (z -10.2) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.167× (z -8.8) |
| [[AN3 CA (line)]] | alt | 34.0 | 0 | 3 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0432× (z -12.3) |
| [[LoVo (line)]] | wt | 20.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.20× (z +15.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.258× (z -9.0) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 9.07 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.59× (z +11.2) | [[Digitoxin (drug)]] 5 µM 0.0773× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.132× (z -9.4) |
| [[SW480 (line)]] | alt | 6.01 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.06× (z +10.9) | — |
| [[CFPAC-1 (line)]] | alt | 9.92 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.19× (z +12.2) | — |
| [[LS 180 (line)]] | wt | 14.8 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +9.8) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.204× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 16.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +11.7) | — |
| [[NCI-H460 (line)]] | wt | 13.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +9.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.130× (z -13.0) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 6.16 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.88× (z +10.4) | — |
| [[SNU-423 (line)]] | alt | 2.44 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.8× (z +9.4) | — |
| [[A-172 (line)]] | wt | 12.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.142× (z -8.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 9.53 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.173× (z -8.8) |
| [[C32 (line)]] | wt | 24.2 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.135× (z -9.7) |
| [[HS-578T (line)]] | alt | 7.70 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +12.7) | — |
| [[J82 (line)]] | alt | 5.57 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -9.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 10.7 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.05 µM 0.176× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 2.47 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.04× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 11.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.167× (z -9.3) |
| [[NCI-H2347 (line)]] | alt | 3.96 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.83× (z +8.8) | — |
| [[RKO (line)]] | wt | 4.91 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.80× (z +9.2) | — |
| [[SK-MEL-2 (line)]] | alt | 7.37 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.31× (z +9.3) | — |
| [[SW1417 (line)]] | alt | 12.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.98× (z +11.2) | — |
| [[A498 (line)]] | wt | 2.07 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.20 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.00 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.14 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.76 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11371), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 35 of them with an alert (⚠; 35 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM202-AS1]] | +0.70 | +0.72 / +0.35 | both halves | 1e-04 |  |
| [[F8]] | +0.69 | +0.74 / +0.34 | both halves | 1e-04 |  |
| [[SEPTIN7-DT]] | +0.68 | +0.71 / +0.29 | both halves | 2e-04 |  |
| [[LINC02542]] | +0.67 | +0.65 / +0.38 | both halves | 7e-05 |  |
| [[PCNX4-DT]] | +0.67 | +0.73 / +0.20 | ⚠ one half (not replicated) | 8e-04 |  |
| [[MZF1-AS1]] | +0.66 | +0.73 / +0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[LINC01135]] | +0.65 | +0.69 / +0.39 | both halves | 5e-05 |  |
| [[C19orf54]] | +0.64 | +0.64 / +0.36 | both halves | 1e-04 |  |
| [[KRCC1]] | +0.64 | +0.75 / +0.16 | ⚠ one half (not replicated) | 0.001 |  |
| [[ENO3]] | +0.63 | +0.69 / +0.30 | both halves | 2e-04 |  |
| [[LEKR1]] | +0.63 | +0.73 / +0.23 | both halves | 5e-04 |  |
| [[MFF-DT]] | +0.63 | +0.59 / +0.27 | both halves | 3e-04 |  |
| [[PCBP1-AS1]] | +0.63 | +0.65 / +0.26 | both halves | 4e-04 |  |
| [[ACAD9-DT]] | +0.63 | +0.65 / +0.34 | both halves | 1e-04 |  |
| [[WAKMAR2]] | +0.62 | +0.61 / +0.25 | both halves | 4e-04 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNA12]] | -0.62 | -0.66 / -0.16 | ⚠ one half (not replicated) | 0.001 | pathway: G alpha (12/13) signalling events |
| [[PCMT1]] | -0.60 | -0.62 / -0.11 | ⚠ one half (not replicated) | 0.002 |  |
| [[LPCAT4]] | -0.59 | -0.66 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[SNRPD2]] | -0.59 | -0.54 / -0.24 | both halves | 5e-04 |  |
| [[FAM118A]] | -0.59 | -0.55 / -0.13 | ⚠ one half (not replicated) | 0.002 |  |
| [[MYPOP]] | -0.58 | -0.57 / -0.23 | both halves | 5e-04 |  |
| [[GTF2E2]] | -0.58 | -0.62 / -0.23 | both halves | 5e-04 |  |
| [[NHP2]] | -0.58 | -0.50 / -0.16 | ⚠ one half (not replicated) | 0.001 |  |
| [[TSEN54]] | -0.57 | -0.54 / -0.19 | ⚠ one half (not replicated) | 8e-04 |  |
| [[MAST3]] | -0.57 | -0.51 / -0.13 | ⚠ one half (not replicated) | 0.002 |  |
| [[MPST]] | -0.57 | -0.57 / -0.22 | both halves | 6e-04 |  |
| [[TRABD]] | -0.56 | -0.54 / -0.22 | both halves | 6e-04 |  |
| [[RNF41]] | -0.56 | -0.52 / -0.22 | both halves | 6e-04 |  |
| [[TNFAIP8L1]] | -0.56 | -0.50 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ARHGEF37's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises ARHGEF37's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ACAA2]] | C | ARHGEF37 activity raises ACAA2's level | lines that do not express ARHGEF37 (4) vs lines expressing it (46) | 2.88× lower at baseline in the lines without ARHGEF37 | 0.018 | ⚠ few lines (4 vs 46); across organs; also absent: DBNDD1, RNFT2, ARFGEF3; maybe low, not absent |
| [[C17orf75]] | C | ARHGEF37 activity raises C17orf75's level | lines that do not express ARHGEF37 (4) vs lines expressing it (46) | 1.65× lower at baseline in the lines without ARHGEF37 | 0.061 | ⚠ few lines (4 vs 46); across organs; also absent: DBNDD1, RNFT2, ARFGEF3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.649). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (6.5, 15.2); signed map (27.0, -9.8). **Vector** length 80.8, 15.5% of its response variance represented; |z| ≥ 3 in 1,038 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.9 | +24.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.3 | +26.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.2 | +12.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.8 | +14.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +12.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.0 | +5.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +7.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +2.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +1.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.0 | +3.6 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | -0.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | +0.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | +2.2 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.7 | -7.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.6 | -4.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.9 | -3.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.3 | -1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | +2.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.2 | -1.1 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.1 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | Rho guanine nucleotide exchange factor 37 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q32 — chr5:149,551,947-149,634,968 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ41603 |
| Gene groups (HGNC) | Dbl family Rho GEFs; BAR and Dbl domain containing; SH3 domain containing |
| Reactome | 7 pathways, smallest: NRAGE signals death through JNK; G alpha (12/13) signalling events; Cell death signalling via NRAGE, NRIF and NADE |
| Matched by | ensembl_id |

**Function**, from UniProt [A1IGU5](https://www.uniprot.org/uniprotkb/A1IGU5) (Rho guanine nucleotide exchange factor 37):

> Probable guanine nucleotide exchange factor (GEF) involved in clathrin-mediated endocytosis, probably playing a role in the late stages of the process.

**Summary**, from NCBI Gene [389337](https://www.ncbi.nlm.nih.gov/gene/389337):

> Predicted to enable guanyl-nucleotide exchange factor activity. Involved in clathrin-dependent endocytosis. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:34430](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:34430) · Entrez [389337](https://www.ncbi.nlm.nih.gov/gene/389337) · UniProt [A1IGU5](https://www.uniprot.org/uniprotkb/A1IGU5) · Ensembl [ENSG00000183111](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183111)

## Data

Gene col 11371: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11371); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11371, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11371]; `tensor/DDL_lfc|DDL_z.npy` [11371]; `embed/gene_vectors.npy` [11371]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11371 or target_col == 11371). Every well: [[ARHGEF37 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGEF37.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
