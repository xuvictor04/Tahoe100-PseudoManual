---
symbol: "PIGM"
type: "gene"
col: 6710
ensembl_id: "ENSG00000143315"
name: "phosphatidylinositol glycan anchor biosynthesis class M"
location: "1q23.2"
module: 16
arm: "+"
pooled_cpm: 10.72
n_lines_expressing: 49
n_dd_up: 19
n_dd_down: 13
n_dd_up_clean: 15
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# PIGM

*phosphatidylinositol glycan anchor biosynthesis class M* — 1q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.18× (z +8.6, q 3e-15, up in 38 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.394× (z -10.6, q 1e-23, down in 37 of 46 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C2orf68]] (+0.69, fdr 7e-06), [[B3GALT9]] (+0.65, fdr 1e-05), [[HERPUD2-AS1]] (+0.63, fdr 1e-05); moves opposite to [[MFSD2B]] (-0.52, fdr 4e-04), [[B4GALT4]] (-0.49, fdr 9e-05), [[NDUFA6]] (-0.48, fdr 3e-04).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6710.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.18×** | +8.6 | 3e-15 | 38/45 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.08×** | +8.3 | 2e-14 | 34/46 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.91×** | +7.4 | 3e-11 | 36/45 (A-172, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.88×** | +7.2 | 8e-11 | 37/46 (NCI-H1573, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.86×** | +6.8 | 1e-09 | 12/22 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.72×** | +6.2 | 5e-08 | 20/33 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +5.9 | 3e-07 | 23/39 (KATO III, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.37×** | +5.0 | 4e-05 | 18/47 (A549, HS-578T, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.56×** | +4.9 | 5e-05 | 19/42 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.49×** | +4.5 | 4e-04 | 17/44 (NCI-H23, HEC-1-A, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.5 | 4e-04 | 21/46 (NCI-H2030, A-172, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +4.5 | 4e-04 | 20/46 (A-172, A-427, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.45×** | +4.2 | 0.001 | 17/46 (A-172, PANC-1, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.45×** | +4.2 | 0.001 | 15/44 (RKO, NCI-H1792, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.008 | 14/46 (SHP-77, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.35×** | +3.3 | 0.032 | 12/44 (KATO III, NCI-H2347, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.67×** | +3.1 | 0.067 | 5/46 (A-172, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.30×** | +3.0 | 0.073 | 4/47 (LS 180, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6710.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.394×** | -10.6 | 1e-23 | 37/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.422×** | -9.8 | 2e-20 | 35/43 (NCI-H23, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.625×** | -7.6 | 6e-12 | 30/45 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.506×** | -7.6 | 6e-12 | 32/45 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.535×** | -6.9 | 5e-10 | 26/44 (RPMI-7951, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.566×** | -6.5 | 8e-09 | 26/46 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.621×** | -5.1 | 2e-05 | 21/44 (SW480, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.495×** | -4.2 | 0.002 | 13/31 (SW480, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.717×** | -3.8 | 0.009 | 16/47 (NCI-H23, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.716×** | -3.7 | 0.012 | 20/45 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.716×** | -3.7 | 0.012 | 20/45 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~15% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.733×** | -3.6 | 0.018 | 11/46 (AN3 CA, KATO III, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.684×** | -3.1 | 0.086 | 14/45 (A498, AN3 CA, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6710. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 20.3 | 0 | 7 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.252× (z -12.1) |
| [[NCI-H23 (line)]] | alt | 27.1 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.119× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.206× (z -11.5) |
| [[NCI-H460 (line)]] | wt | 14.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -10.1) |
| [[PANC-1 (line)]] | alt | 9.30 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -14.6) |
| [[LoVo (line)]] | wt | 8.74 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.152× (z -10.2) |
| [[A498 (line)]] | wt | 3.74 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -9.7) |
| [[COLO 205 (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.103× (z -9.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 14.3 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.42× (z +8.5) ⚠ toxic | — |
| [[LS 180 (line)]] | wt | 7.62 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0903× (z -9.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 11.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.132× (z -9.7) ⚠ cell-cycle shift, explains ~65% of this change |
| [[RKO (line)]] | wt | 13.7 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.156× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 11.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.111× (z -10.1) |
| [[A-172 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.60 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.62 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.64 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.30 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.04 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.24 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.16 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.43 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.46 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6710), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C2orf68]] | +0.69 | +0.66 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[B3GALT9]] | +0.65 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[HERPUD2-AS1]] | +0.63 | +0.72 / +0.53 | both halves | 1e-05 |  |
| [[RAB4A-AS1]] | +0.58 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[PLPP6]] | +0.54 | +0.68 / +0.43 | both halves | 3e-05 |  |
| [[MAGEF1]] | +0.54 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[TMEM177]] | +0.53 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[ATXN7L3B]] | +0.53 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[COG2]] | +0.53 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[COG8]] | +0.52 | +0.58 / +0.46 | both halves | 2e-05 |  |
| [[MSL3P1]] | +0.52 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[EID1]] | +0.52 | +0.55 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFSD2B]] | -0.52 | -0.26 / -0.41 | both halves | 4e-04 |  |
| [[B4GALT4]] | -0.49 | -0.39 / -0.36 | both halves | 9e-05 |  |
| [[NDUFA6]] | -0.48 | -0.28 / -0.34 | both halves | 3e-04 |  |
| [[DRC1]] | -0.46 | -0.28 / -0.26 | both halves | 4e-04 |  |
| [[C9orf24]] | -0.46 | -0.36 / -0.36 | both halves | 1e-04 |  |
| [[TRNAU1AP]] | -0.45 | -0.39 / -0.27 | both halves | 3e-04 |  |
| [[MCF2]] | -0.45 | -0.23 / -0.37 | both halves | 5e-04 |  |
| [[SNHG12]] | -0.45 | -0.36 / -0.27 | both halves | 3e-04 |  |
| [[SOS1]] | -0.45 | -0.42 / -0.37 | both halves | 9e-05 |  |
| [[LINC03016]] | -0.44 | -0.24 / -0.29 | both halves | 5e-04 |  |
| [[CCDC17]] | -0.44 | -0.18 / -0.39 | ⚠ not reproduced | 1e-03 |  |
| [[LINC02936]] | -0.44 | -0.31 / -0.26 | both halves | 4e-04 |  |
| [[PRDM2]] | -0.44 | -0.22 / -0.36 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises PIGM's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[RNFT2]] | C | RNFT2 activity raises PIGM's level | lines that do not express RNFT2 (3) vs lines expressing it (47) | 2.37× lower at baseline in the lines without RNFT2 | 0.066 | ⚠ few lines (3 vs 47); across organs; also absent: ARHGEF37, CSRP1-AS1, DBNDD1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.363). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-36.3, 18.0); signed map (-1.5, -31.2). **Vector** length 58.8, 9.36% of its response variance represented; |z| ≥ 3 in 956 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | +1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +4.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | -1.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.0 | +5.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +1.8 | +7.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.3 | +0.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.2 | +3.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.1 | +4.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -0.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.3 | -6.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.3 | -7.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.9 | -5.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -3.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.5 | -3.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.4 | -3.1 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.4 | -2.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.1 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol glycan anchor biosynthesis class M |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.2 — chr1:160,024,953-160,031,990 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GPI-MT-I, PIG-M |
| Gene groups (HGNC) | Dolichyl D-mannosyl phosphate dependent mannosyltransferases; Phosphatidylinositol glycan anchor biosynthesis |
| Reactome | 2 pathways, smallest: Synthesis of glycosylphosphatidylinositol (GPI); Post-translational modification: synthesis of GPI-anchored proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H3S5](https://www.uniprot.org/uniprotkb/Q9H3S5) (GPI alpha-1,4-mannosyltransferase I, catalytic subunit):

> Catalytic subunit of the glycosylphosphatidylinositol-mannosyltransferase I complex which catalyzes the transfer of the first mannose, via an alpha-1,4 bond from a dolichol-phosphate-mannose (Dol-P-Man) to a 2-acyl-6-alpha-D-glucosaminyl-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol (glucosaminyl acyl phosphatidylinositol, GlcN-(acyl)PI) intermediate to generate 2-acyl-6-(alpha-D-mannosyl-(1->4)-alpha-D-glucosaminyl)-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol (also termed …

**Summary**, from NCBI Gene [93183](https://www.ncbi.nlm.nih.gov/gene/93183):

> This gene encodes a transmembrane protein that is located in the endoplasmic reticulum and is involved in GPI-anchor biosynthesis. The glycosylphosphatidylinositol (GPI)-anchor is a glycolipid which contains three mannose molecules in its core backbone. The GPI-anchor is found on many blood cells and serves to anchor proteins to the cell surface. This gene encodes a mannosyltransferase, GPI-MT-I, that transfers the first mannose to GPI on the lumenal side of the endoplasmic reticulum. [provided …

**Accessions** — [HGNC:18858](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18858) · Entrez [93183](https://www.ncbi.nlm.nih.gov/gene/93183) · UniProt [Q9H3S5](https://www.uniprot.org/uniprotkb/Q9H3S5) · Ensembl [ENSG00000143315](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143315)

## Data

Gene col 6710: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6710); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6710, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6710]; `tensor/DDL_lfc|DDL_z.npy` [6710]; `embed/gene_vectors.npy` [6710]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6710 or target_col == 6710). Every well: [[PIGM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIGM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
