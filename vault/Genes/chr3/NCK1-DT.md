---
symbol: "NCK1-DT"
type: "gene"
col: 14183
ensembl_id: "ENSG00000239213"
name: "NCK1 divergent transcript"
location: "3q22.3"
module: 21
arm: "+"
pooled_cpm: 12.15
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 18
n_dd_up_clean: 17
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# NCK1-DT

*NCK1 divergent transcript* — 3q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.02× (z +14.2, q 9e-43, up in 39 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.593× (z -7.4, q 8e-11, down in 26 of 46 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APTR]] (+0.64, fdr 1e-05), [[C12orf73]] (+0.61, fdr 2e-05), [[FAM151B-DT]] (+0.58, fdr 1e-05); moves opposite to [[PSMC5]] (-0.53, fdr 1e-04), [[PUF60]] (-0.53, fdr 3e-04), [[PSMG1]] (-0.53, fdr 2e-04).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PCNX2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14183.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.02×** | +14.2 | 9e-43 | 39/45 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~5% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.39×** | +11.9 | 2e-30 | 33/44 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.31×** | +11.9 | 2e-30 | 40/47 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.14×** | +10.8 | 5e-25 | 38/48 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.81×** | +8.5 | 3e-15 | 33/48 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.51×** | +8.3 | 1e-14 | 37/48 (J82, A-427, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +7.7 | 9e-13 | 31/46 (SW480, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~5% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.99×** | +7.6 | 1e-12 | 28/48 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.66×** | +7.2 | 4e-11 | 27/46 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.09×** | +5.5 | 2e-06 | 20/47 (SW480, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.58×** | +5.1 | 2e-05 | 20/43 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.26×** | +4.7 | 1e-04 | 18/48 (SNU-423, RKO, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +4.6 | 2e-04 | 18/47 (KATO III, SNU-423, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.30×** | +3.7 | 0.009 | 8/47 (SW480, KATO III, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.20× | +3.6 | 0.013 | 11/48 (PANC-1, SW480, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.18× | +3.2 | 0.046 | 12/48 (SW480, CFPAC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14183.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.593×** | -7.4 | 8e-11 | 26/46 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.613×** | -6.9 | 1e-09 | 26/47 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.655×** | -6.0 | 4e-07 | 26/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.621×** | -5.3 | 2e-05 | 21/47 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.631×** | -5.1 | 3e-05 | 21/46 (PANC-1, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.697×** | -5.1 | 3e-05 | 19/44 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.741×** | -4.0 | 0.005 | 21/45 (A498, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.761×** | -3.9 | 0.008 | 15/47 (HT-29, CFPAC-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.596×** | -3.8 | 0.008 | 16/43 (COLO 205, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.757×** | -3.8 | 0.009 | 20/47 (A498, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.925× | -3.6 | 0.019 | 7/48 (NCI-H2347, AN3 CA, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.627×** | -3.5 | 0.023 | 9/48 (NCI-H1573, Hs 766T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.783×** | -3.5 | 0.023 | 14/48 (SW 1088, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.783×** | -3.5 | 0.023 | 14/48 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.785×** | -3.4 | 0.023 | 7/47 (CFPAC-1, RPMI-7951, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.794×** | -3.3 | 0.039 | 13/48 (SW 1088, BT-474, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.853× | -3.2 | 0.052 | 8/48 (CFPAC-1, LoVo, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.807×** | -3.0 | 0.076 | 10/47 (BT-474, SK-MEL-2, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.813×** | -2.9 | 0.098 | 9/47 (H4, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14183. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 15.6 | 2 | 2 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +9.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.339× (z -9.4) |
| [[A-427 (line)]] | wt | 18.4 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 16.2 | 3 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 10.3 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.17× (z +9.3) | — |
| [[A-172 (line)]] | wt | 7.03 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.87× (z +8.7) | — |
| [[BT-474 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.110× (z -10.4) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 14.2 | 0 | 1 | — | [[Hydroxyfasudil (drug)]] 5 µM 0.0334× (z -10.5) |
| [[HS-578T (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.107× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 14.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.142× (z -10.7) ⚠ toxic; cell-cycle shift, explains ~21% of this change |
| [[SNU-423 (line)]] | alt | 6.83 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.0777× (z -10.1) |
| [[SW 900 (line)]] | alt | 8.37 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0786× (z -9.7) |
| [[A498 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.65 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.76 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.79 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.70 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.87 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.72 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.08 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.56 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.82 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.10 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14183), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APTR]] | +0.64 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[C12orf73]] | +0.61 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[FAM151B-DT]] | +0.58 | +0.55 / +0.55 | both halves | 1e-05 | same gene group |
| [[MCEE]] | +0.56 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[GPBP1L1]] | +0.56 | +0.31 / +0.38 | both halves | 2e-04 |  |
| [[HOXB6]] | +0.56 | +0.40 / +0.53 | both halves | 5e-05 |  |
| [[SLC15A2]] | +0.55 | +0.46 / +0.66 | both halves | 3e-05 |  |
| [[GNAS]] | +0.55 | +0.39 / +0.33 | both halves | 1e-04 |  |
| [[SERF2]] | +0.55 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[FAM217A]] | +0.55 | +0.35 / +0.51 | both halves | 1e-04 |  |
| [[EAF2]] | +0.55 | +0.43 / +0.72 | both halves | 3e-05 |  |
| [[EOGT-DT]] | +0.54 | +0.35 / +0.55 | both halves | 1e-04 | same gene group |

## Genes that move opposite

*25 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMC5]] | -0.53 | -0.32 / -0.47 | both halves | 1e-04 |  |
| [[PUF60]] | -0.53 | -0.27 / -0.59 | both halves | 3e-04 |  |
| [[PSMG1]] | -0.53 | -0.32 / -0.39 | both halves | 2e-04 |  |
| [[RNF123]] | -0.52 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[EIF6]] | -0.52 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[POGK]] | -0.52 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[ZKSCAN2]] | -0.52 | -0.14 / -0.50 | ⚠ not reproduced | 0.002 |  |
| [[TMEM185B]] | -0.51 | -0.24 / -0.51 | both halves | 5e-04 |  |
| [[TRMT61A]] | -0.51 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[ZFP1]] | -0.51 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[FKTN]] | -0.50 | -0.30 / -0.39 | both halves | 2e-04 |  |
| [[PSMC3]] | -0.50 | -0.30 / -0.60 | both halves | 2e-04 |  |
| [[DRG2]] | -0.50 | -0.28 / -0.37 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCNX2]] | B | PCNX2 activity raises NCK1-DT's level | lines that do not express PCNX2 (8) vs lines expressing it (42) | 1.37× lower at baseline in the lines without PCNX2 | 0.081 | ⚠ within organs, on part of the lines; also absent: NAALADL2, PLEKHA5, KLHL29; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.463). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.3, 28.6); signed map (19.8, -0.2). **Vector** length 56.8, 8.42% of its response variance represented; |z| ≥ 3 in 1,029 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +11.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.1 | +14.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +1.9 | +7.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +1.8 | +7.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +8.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.4 | +2.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.3 | +3.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.3 | +2.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.3 | +3.7 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -3.5 | -6.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -5.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.6 | -7.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.4 | -4.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | -0.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -3.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.5 | -0.3 |
|  | [[EX229 (drug)]] 5 µM |  | -1.5 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | NCK1 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3q22.3 — chr3:136,835,345-136,862,618 (-) |
| Ensembl biotype | lncRNA |
| Also known as | SLC35G2-AS1; previously NCK1-AS1 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:49645](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49645) · Entrez [101927597](https://www.ncbi.nlm.nih.gov/gene/101927597) · Ensembl [ENSG00000239213](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000239213)

## Data

Gene col 14183: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14183); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14183, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14183]; `tensor/DDL_lfc|DDL_z.npy` [14183]; `embed/gene_vectors.npy` [14183]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14183 or target_col == 14183). Every well: [[NCK1-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NCK1-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
