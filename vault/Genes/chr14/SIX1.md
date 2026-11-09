---
symbol: "SIX1"
type: "gene"
col: 4764
ensembl_id: "ENSG00000126778"
name: "SIX homeobox 1"
location: "14q23.1"
module: 70
arm: "+"
pooled_cpm: 9.34
n_lines_expressing: 42
n_dd_up: 15
n_dd_down: 2
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 19
tags: ["gene", "module/070", "written"]
generated_by: "tahoemap"
---

# SIX1

*SIX homeobox 1* — 14q23.1

> [!summary] In one line
> SIX1 is a homeodomain transcription factor that, paired with an EYA cofactor, switches from repressor to activator and drives the embryonic muscle, otic and kidney programmes.

## What it is

SIX1 is a vertebrate homologue of Drosophila sine oculis. Bound through its homeodomain and SIX domain it recruits DACH proteins and co-repressors; when an EYA protein joins, the output flips to activation, EYA's phosphatase activity being part of the switch. The SIX1-EYA module sits near the top of the skeletal muscle hierarchy, required for normal PAX3 and myogenic-regulatory-factor expression and later for the fast-twitch programme, and it also builds the otic and nephric lineages — mutations disrupting the EYA1-SIX1-DNA interface cause branchio-oto-renal syndrome. In carcinomas it is often overexpressed and reported to promote epithelial-mesenchymal transition.

## What is uncertain

Its curated target set is small, so an activity inferred from it is near an average over a handful of transcripts, and small target sets reach a ranking's extremes cheaply. Those targets come from myogenic work, the context these lines lack, so what moved may belong to other regulators.

## References

- Ruf et al., 2004, PNAS — SIX1 mutations cause branchio-oto-renal syndrome by disrupting EYA1-SIX1-DNA complexes.
- Li et al., 2003, Nature — EYA phosphatase activity converts the SIX1-DACH-EYA complex from repression to activation.
- Grifone et al., 2005, Development — Six1 and Six4 are required for Pax3 and myogenic regulatory factor expression during myogenesis.
- Laclef et al., 2003, Development — Six1-null mice show altered myogenesis and muscle patterning defects.
- Micalizzi et al., 2009, Journal of Clinical Investigation — SIX1 overexpression promotes epithelial-mesenchymal transition via TGF-beta signalling.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.42× (z +11.7, q 1e-28, up in 29 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.539× (z -5.8, q 3e-06, down in 23 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (SHP-77 0.137×, HS-578T 0.0943×, NCI-H2030 0.141×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (AN3 CA 0.0985×, Hs 766T 0.202×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A498 0.0898×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATRIP]] (+0.60, fdr 5e-05), [[PSMB10]] (+0.58, fdr 1e-04), [[DDX24]] (+0.58, fdr 7e-05); moves opposite to [[CTC1]] (-0.59, fdr 4e-05), [[GALNS]] (-0.52, fdr 3e-05), [[ZC3H3]] (-0.50, fdr 5e-04).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 19 go from it, the strongest it → cells under [[Lonafarnib (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4764.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.42×** | +11.7 | 1e-28 | 29/34 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.44×** | +8.0 | 3e-13 | 24/34 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.67×** | +4.6 | 8e-04 | 16/32 (NCI-H460, C-33 A, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +4.5 | 0.001 | 19/34 (A-427, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +3.9 | 0.009 | 5/40 (HOP62, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | **1.34×** | +3.8 | 0.012 | 11/39 (NCI-H460, SW480, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **1.50×** | +3.8 | 0.012 | 12/33 (NCI-H2347, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.47×** | +3.6 | 0.026 | 15/36 (SW 900, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~23% here); position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.30×** | +3.4 | 0.035 | 14/39 (MIA PaCa-2, SK-MEL-2, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.44×** | +3.4 | 0.038 | 13/39 (NCI-H1573, CFPAC-1, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.41×** | +3.2 | 0.070 | 14/39 (CFPAC-1, NCI-H1573, …) | all doses, flat |  |
| [[Rosiglitazone (drug)]] 5 µM |  | **1.42×** | +3.2 | 0.070 | 3/36 (NCI-H2030, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.41×** | +3.2 | 0.070 | 15/39 (NCI-H1573, CFPAC-1, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.39×** | +3.1 | 0.083 | 15/39 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.0 | 0.092 | 14/40 (SW 900, CFPAC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.38×** | +3.0 | 0.097 | 10/35 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4764.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (SHP-77 0.137×, HS-578T 0.0943×, NCI-H2030 0.141×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (AN3 CA 0.0985×, Hs 766T 0.202×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A498 0.0898×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.539×** | -5.8 | 3e-06 | 23/39 (SNU-423, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.648×** | -3.8 | 0.043 | 17/24 (SHP-77, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.694× | -3.5 | 0.10 | 15/38 (NCI-H1573, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | 0.525× | -3.2 | 0.21 | 14/37 (J82, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.722× | -3.1 | 0.23 | 13/38 (PANC-1, A498, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4764. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 8.29 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0943× (z -9.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 7.79 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0898× (z -12.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 6.85 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.18× (z +10.5) | — |
| [[AN3 CA (line)]] | alt | 49.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0985× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 11.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.05× (z +9.4) | — |
| [[H4 (line)]] | wt | 13.8 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0544× (z -9.7) ⚠ cell-cycle shift, explains ~88% of this change |
| [[Hs 766T (line)]] | wt | 39.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 12.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.67× (z +9.2) | — |
| [[NCI-H2030 (line)]] | alt | 11.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.141× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 7.68 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.78× (z +12.2) | — |
| [[SHP-77 (line)]] | alt | 20.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.137× (z -9.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 5.80 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.55× (z +8.7) | — |
| [[A-172 (line)]] | wt | 4.70 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.36 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.797 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.982 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.708 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.95 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.22 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.883 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.806 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.867 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.925 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4764), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATRIP]] | +0.60 | +0.40 / +0.68 | both halves | 5e-05 |  |
| [[PSMB10]] | +0.58 | +0.36 / +0.64 | both halves | 1e-04 |  |
| [[DDX24]] | +0.58 | +0.38 / +0.59 | both halves | 7e-05 |  |
| [[PSMB9]] | +0.57 | +0.39 / +0.64 | both halves | 5e-05 |  |
| [[IRX5]] | +0.56 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[ENDOG]] | +0.56 | +0.33 / +0.60 | both halves | 1e-04 |  |
| [[CBR3]] | +0.56 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[DLX1]] | +0.55 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[IRF2]] | +0.54 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[UBE2L6]] | +0.54 | +0.31 / +0.60 | both halves | 2e-04 |  |
| [[MRPL36]] | +0.53 | +0.40 / +0.61 | both halves | 5e-05 |  |
| [[GBP4]] | +0.53 | +0.44 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTC1]] | -0.59 | -0.41 / -0.63 | both halves | 4e-05 |  |
| [[GALNS]] | -0.52 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[ZC3H3]] | -0.50 | -0.24 / -0.59 | both halves | 5e-04 |  |
| [[LINC03009]] | -0.50 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[VAMP7]] | -0.49 | -0.33 / -0.57 | both halves | 1e-04 |  |
| [[RAD51-AS1]] | -0.49 | -0.28 / -0.58 | both halves | 3e-04 |  |
| [[LENG8]] | -0.48 | -0.37 / -0.55 | both halves | 9e-05 |  |
| [[AGO1]] | -0.48 | -0.26 / -0.59 | both halves | 4e-04 |  |
| [[DPY19L4]] | -0.48 | -0.09 / -0.62 | ⚠ one half (not replicated) | 0.003 |  |
| [[EIF2S3]] | -0.48 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[MORF4L1]] | -0.48 | -0.32 / -0.52 | both halves | 2e-04 |  |
| [[DHFR]] | -0.48 | -0.25 / -0.60 | both halves | 4e-04 |  |
| [[CDA]] | -0.47 | -0.45 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SIX1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 0, C 19. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Lonafarnib (drug)]] 5 µM | C | SIX1 activity raises the cells' numbers under Lonafarnib 5 µM (protects the cells) | lines that do not express SIX1 (8) vs lines expressing it (40) | the lines without SIX1: 0.20× the cells of the other lines | 0.008 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: TIGD7, ENSG00000286964, FERMT2 |
| cells under [[Almonertinib (hydrochloride) (drug)]] 0.5 µM | C | SIX1 activity raises the cells' numbers under Almonertinib (hydrochloride) 0.5 µM (protects the cells) | lines that do not express SIX1 (8) vs lines expressing it (40) | the lines without SIX1: 0.82× the cells of the other lines | 0.014 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: TIGD7, ENSG00000286964, FERMT2 |
| cells under [[BAY1125976 (drug)]] 0.5 µM | C | SIX1 activity raises the cells' numbers under BAY1125976 0.5 µM (protects the cells) | lines that do not express SIX1 (8) vs lines expressing it (40) | the lines without SIX1: 0.76× the cells of the other lines | 0.022 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: TIGD7, ENSG00000286964, FERMT2 |
| cells under [[Erlotinib (drug)]] 0.05 µM | C | SIX1 activity lowers the cells' numbers under Erlotinib 0.05 µM (makes them more sensitive) | lines that do not express SIX1 (8) vs lines expressing it (40) | the lines without SIX1: 1.26× the cells of the other lines | 0.025 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: TIGD7, ENSG00000286964, FERMT2 |
| cells under [[Furosemide (drug)]] 0.5 µM | C | SIX1 activity lowers the cells' numbers under Furosemide 0.5 µM (makes them more sensitive) | lines that do not express SIX1 (8) vs lines expressing it (40) | the lines without SIX1: 1.21× the cells of the other lines | 0.026 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: TIGD7, ENSG00000286964, FERMT2 |
| cells under [[Mifepristone (drug)]] 0.5 µM | C | SIX1 activity raises the cells' numbers under Mifepristone 0.5 µM (protects the cells) | lines that do not express SIX1 (8) vs lines expressing it (40) | the lines without SIX1: 0.82× the cells of the other lines | 0.027 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: TIGD7, ENSG00000286964, FERMT2 |
| cells under [[Dihydroartemisinin (drug)]] 5 µM | C | SIX1 activity lowers the cells' numbers under Dihydroartemisinin 5 µM (makes them more sensitive) | lines that do not express SIX1 (8) vs lines expressing it (40) | the lines without SIX1: 1.36× the cells of the other lines | 0.031 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: TIGD7, ENSG00000286964, FERMT2 |
| cells under [[9-ING-41 (drug)]] 0.5 µM | C | SIX1 activity raises the cells' numbers under 9-ING-41 0.5 µM (protects the cells) | lines that do not express SIX1 (8) vs lines expressing it (40) | the lines without SIX1: 0.82× the cells of the other lines | 0.032 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: TIGD7, ENSG00000286964, FERMT2 |
| cells under [[Menadione (drug)]] 0.5 µM | C | SIX1 activity lowers the cells' numbers under Menadione 0.5 µM (makes them more sensitive) | lines that do not express SIX1 (8) vs lines expressing it (40) | the lines without SIX1: 1.18× the cells of the other lines | 0.034 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: TIGD7, ENSG00000286964, FERMT2 |
| cells under [[Rucaparib (phosphate) (drug)]] 0.5 µM | C | SIX1 activity raises the cells' numbers under Rucaparib (phosphate) 0.5 µM (protects the cells) | lines that do not express SIX1 (8) vs lines expressing it (40) | the lines without SIX1: 0.85× the cells of the other lines | 0.053 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: TIGD7, ENSG00000286964, FERMT2 |
| cells under [[AZD2858 (drug)]] 5 µM | C | SIX1 activity lowers the cells' numbers under AZD2858 5 µM (makes them more sensitive) | lines that do not express SIX1 (8) vs lines expressing it (40) | the lines without SIX1: 1.33× the cells of the other lines | 0.059 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: TIGD7, ENSG00000286964, FERMT2 |
| cells under [[Glasdegib (drug)]] 5 µM | C | SIX1 activity lowers the cells' numbers under Glasdegib 5 µM (makes them more sensitive) | lines that do not express SIX1 (8) vs lines expressing it (40) | the lines without SIX1: 1.21× the cells of the other lines | 0.063 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: TIGD7, ENSG00000286964, FERMT2; cell counts less trustworthy |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.510). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (26.4, -36.8); signed map (17.3, -10.7). **Vector** length 70.4, 15.1% of its response variance represented; |z| ≥ 3 in 684 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +11.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +8.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +2.4 | +4.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +1.9 | +3.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.7 | +2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.4 | +2.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.1 | -1.6 |
|  | [[Carbamazepine (drug)]] 5 µM |  | +1.1 | +2.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.1 | +1.7 |
|  | [[AZD-7648 (drug)]] 5 µM |  | +1.0 | +2.7 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -5.1 | -1.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.9 | -3.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.8 | -2.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | -1.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.6 | -2.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.5 | -1.8 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.5 | -1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | SIX homeobox 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q23.1 — chr14:60,643,421-60,658,259 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously DFNA23 |
| Gene groups (HGNC) | SINE class homeoboxes |
| Reactome | 2 pathways, smallest: Formation of the ureteric bud; Kidney development |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15475](https://www.uniprot.org/uniprotkb/Q15475) (Homeobox protein SIX1):

> Transcription factor that is involved in the regulation of cell proliferation, apoptosis and embryonic development (By similarity). Plays an important role in the development of several organs, including kidney, muscle and inner ear (By similarity). Depending on context, functions as a transcriptional repressor or activator (By similarity). Lacks an activation domain, and requires interaction with EYA family members for transcription activation. Mediates nuclear translocation of EYA1 and EYA2. …

**Summary**, from NCBI Gene [6495](https://www.ncbi.nlm.nih.gov/gene/6495):

> The protein encoded by this gene is a homeobox protein that is similar to the Drosophila 'sine oculis' gene product. This gene is found in a cluster of related genes on chromosome 14 and is thought to be involved in limb development. Defects in this gene are a cause of autosomal dominant deafness type 23 (DFNA23) and branchiootic syndrome type 3 (BOS3). [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:10887](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10887) · Entrez [6495](https://www.ncbi.nlm.nih.gov/gene/6495) · UniProt [Q15475](https://www.uniprot.org/uniprotkb/Q15475) · Ensembl [ENSG00000126778](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126778)

## Data

Gene col 4764: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4764); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4764, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4764]; `tensor/DDL_lfc|DDL_z.npy` [4764]; `embed/gene_vectors.npy` [4764]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4764 or target_col == 4764). Every well: [[SIX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/SIX1.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
