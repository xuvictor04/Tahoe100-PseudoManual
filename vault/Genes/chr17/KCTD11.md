---
symbol: "KCTD11"
type: "gene"
col: 13141
ensembl_id: "ENSG00000213859"
name: "potassium channel tetramerization domain containing 11"
location: "17p13.1"
module: 20
arm: "-"
pooled_cpm: 15.95
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 17
n_dd_up_clean: 4
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# KCTD11

*potassium channel tetramerization domain containing 11* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 2.46× (z +7.5, q 4e-11, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.427× (z -6.8, q 6e-09, down in 31 of 42 measured lines) ⚠ toxic. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.451× (z -6.6, q 1e-08, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IER5]] (+0.72, fdr 7e-06), [[SERTAD1]] (+0.67, fdr 7e-06), [[FOXD1]] (+0.65, fdr 7e-06); moves opposite to [[DFFB]] (-0.67, fdr 7e-06), [[SACM1L]] (-0.61, fdr 7e-06), [[NUDT21]] (-0.57, fdr 3e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CLDN14-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13141.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **2.46×** | +7.5 | 4e-11 | 36/47 (HOP62, A549, …) | inconsistent across doses | cell-cycle shift (explains ~6% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.09×** | +6.1 | 3e-07 | 33/47 (A-172, A549, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **2.03×** | +5.9 | 7e-07 | 34/46 (A-172, A-427, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +3.9 | 0.014 | 25/45 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **2.29×** | +3.6 | 0.036 | 21/44 (HOP62, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 1.45× | +3.1 | 0.17 | 11/46 (A-172, NCI-H23, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13141.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.427×** | -6.8 | 6e-09 | 31/42 (J82, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.451×** | -6.6 | 1e-08 | 34/47 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.533×** | -4.9 | 1e-04 | 30/46 (NCI-H23, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.571×** | -4.7 | 5e-04 | 27/48 (HOP62, AsPC-1, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.692×** | -4.3 | 0.002 | 23/45 (CFPAC-1, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~16% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.388×** | -4.1 | 0.004 | 19/36 (PANC-1, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.612×** | -4.1 | 0.004 | 25/48 (HT-29, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.420×** | -3.8 | 0.012 | 21/46 (CFPAC-1, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.654×** | -3.5 | 0.027 | 16/47 (SW480, PANC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.642×** | -3.5 | 0.028 | 22/47 (LS 180, LoVo, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.659×** | -3.5 | 0.028 | 20/47 (HOP62, NCI-H23, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.653×** | -3.4 | 0.031 | 25/45 (SW 900, PANC-1, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.466×** | -3.3 | 0.039 | 17/43 (Hs 766T, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | **0.683×** | -3.2 | 0.056 | 20/48 (HOP62, A498, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 5 µM |  | **0.483×** | -3.2 | 0.056 | 12/47 (PANC-1, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.684×** | -3.2 | 0.056 | 17/48 (HS-578T, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.687×** | -3.1 | 0.060 | 19/47 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13141. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 24.1 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.28× (z +11.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 4.82× (z +8.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0762× (z -13.5) ⚠ toxic |
| [[HCT15 (line)]] | alt | 43.2 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 24.4 | 2 (1 ⚠) | 1 | [[Harringtonine (drug)]] 0.5 µM 7.20× (z +11.3) | [[Ixazomib citrate (drug)]] 5 µM 0.156× (z -10.6) |
| [[A-172 (line)]] | wt | 28.5 | 2 | 0 | [[Auranofin (drug)]] 5 µM 5.01× (z +9.5) | — |
| [[A549 (line)]] | wt | 17.6 | 2 | 0 | [[Harringtonine (drug)]] 0.5 µM 8.99× (z +10.9) | — |
| [[AsPC-1 (line)]] | alt | 18.8 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.09× (z +9.6) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[CFPAC-1 (line)]] | alt | 30.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 7.79 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 8.12× (z +11.3) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[SW480 (line)]] | alt | 30.1 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 4.57× (z +10.0) | — |
| [[Hs 766T (line)]] | wt | 22.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.113× (z -10.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 27.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0296× (z -19.3) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 18.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.141× (z -9.8) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 14.6 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0452× (z -10.3) ⚠ toxic |
| [[SW 900 (line)]] | alt | 13.5 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 10.5× (z +9.6) | — |
| [[SW48 (line)]] | wt | 11.7 | 0 | 1 | — | [[Nevirapine (drug)]] 0.05 µM 0.0627× (z -8.8) |
| [[A-427 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.30 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.18 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.75 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.89 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.95 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13141), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IER5]] | +0.72 | +0.59 / +0.72 | both halves | 7e-06 |  |
| [[SERTAD1]] | +0.67 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[FOXD1]] | +0.65 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[PPP1R14B-AS1]] | +0.62 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[METTL23]] | +0.62 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[GALE]] | +0.62 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[MFAP1]] | +0.60 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[ARRDC4]] | +0.58 | +0.64 / +0.46 | both halves | 2e-05 |  |
| [[RSPH3]] | +0.58 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[ACAP1]] | +0.58 | +0.51 / +0.60 | both halves | 1e-05 | ⚠ same locus (0.4 kb, same strand: neighbours can correlate without regulation) |
| [[SRSF9]] ⚠ | +0.57 | +0.60 / +0.63 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[SERTAD2]] | +0.57 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[CDIP1]] | +0.57 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[BTG1]] | +0.57 | +0.53 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DFFB]] | -0.67 | -0.63 / -0.63 | both halves | 7e-06 |  |
| [[SACM1L]] | -0.61 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[NUDT21]] | -0.57 | -0.44 / -0.69 | both halves | 3e-05 |  |
| [[POLR2B]] | -0.57 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[CIZ1]] | -0.57 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[SKP2]] | -0.57 | -0.51 / -0.67 | both halves | 1e-05 |  |
| [[UTP18]] | -0.55 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[RAVER2]] | -0.54 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[HADH]] | -0.54 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[ANAPC5]] | -0.54 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[MRE11]] | -0.54 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[RPA1]] | -0.53 | -0.42 / -0.64 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLDN14-AS1]] | B | CLDN14-AS1 activity raises KCTD11's level | lines that do not express CLDN14-AS1 (16) vs lines expressing it (34) | 1.46× lower at baseline in the lines without CLDN14-AS1 | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000230479, ENSG00000289526, TMEM158 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.495). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-2.5, -22.8); signed map (3.7, 24.0). **Vector** length 120, 33.0% of its response variance represented; |z| ≥ 3 in 1,036 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +7.3 | +7.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.7 | +5.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.3 | +6.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | +4.7 | +1.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +4.5 | +2.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.8 | +2.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.6 | +3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +1.6 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -8.0 | -6.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.0 | -1.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.7 | +0.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.4 | -6.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -5.2 | +1.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.7 | -2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.5 | -4.7 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -3.2 | -2.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.1 | -3.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.6 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | potassium channel tetramerization domain containing 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:7,351,889-7,354,944 (+) |
| Ensembl biotype | protein_coding |
| Also known as | REN, KCASH1; previously C17orf36 |
| Gene groups (HGNC) | KCTD family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q693B1](https://www.uniprot.org/uniprotkb/Q693B1) (BTB/POZ domain-containing protein KCTD11):

> Plays a role as a marker and a regulator of neuronal differentiation; Up-regulated by a variety of neurogenic signals, such as retinoic acid, epidermal growth factor/EGF and NGFB/nerve growth factor. Induces apoptosis, growth arrest and the expression of cyclin-dependent kinase inhibitor CDKN1B. Plays a role as a tumor repressor and inhibits cell growth and tumorigenicity of medulloblastoma (MDB). Acts as a probable substrate-specific adapter for a BCR (BTB-CUL3-RBX1) E3 ubiquitin-protein …

**Summary**, from NCBI Gene [147040](https://www.ncbi.nlm.nih.gov/gene/147040):

> Enables identical protein binding activity. Predicted to be involved in positive regulation of neuron differentiation. Predicted to act upstream of or within several processes, including negative regulation of neuroblast proliferation; negative regulation of smoothened signaling pathway; and nervous system development. Predicted to be located in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21302](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21302) · Entrez [147040](https://www.ncbi.nlm.nih.gov/gene/147040) · UniProt [Q693B1](https://www.uniprot.org/uniprotkb/Q693B1) · Ensembl [ENSG00000213859](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213859)

## Data

Gene col 13141: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13141); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13141, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13141]; `tensor/DDL_lfc|DDL_z.npy` [13141]; `embed/gene_vectors.npy` [13141]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13141 or target_col == 13141). Every well: [[KCTD11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCTD11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
