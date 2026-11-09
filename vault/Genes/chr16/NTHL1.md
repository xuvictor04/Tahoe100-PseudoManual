---
symbol: "NTHL1"
type: "gene"
col: 771
ensembl_id: "ENSG00000065057"
name: "nth like DNA glycosylase 1"
location: "16p13.3"
module: 58
arm: "+"
pooled_cpm: 5.37
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 10
n_dd_up_clean: 3
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# NTHL1

*nth like DNA glycosylase 1* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.61× (z +7.1, q 6e-10, up in 16 of 24 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.81× (z +4.4, q 0.002, up in 24 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.248× (z -10.3, q 2e-22, down in 41 of 46 measured lines).
> Its strongest partners by |cos| (78 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 27 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPS34]] (+0.65, fdr 6e-04), [[NDUFB10]] (+0.64, fdr 5e-05), [[PAXX]] (+0.62, fdr 4e-04, ⚠ PAXX in the vector space only through flagged drug-doses), [[RP9]] (+0.62, fdr 1e-05); moves opposite to [[CERS2]] (-0.63, fdr 2e-05), [[SAP30L-AS1]] (-0.58, fdr 2e-04), [[SNHG22]] (-0.58, fdr 2e-04).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FSTL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 771.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.61×** | +7.1 | 6e-10 | 16/24 (HT-29, CFPAC-1, …) | two highest doses | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.20×** | +5.7 | 4e-06 | 4/8 (A498, AsPC-1, …) | two highest doses | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.81×** | +4.4 | 0.002 | 24/45 (A-172, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.74×** | +4.1 | 0.005 | 21/47 (NCI-H1792, NCI-H1573, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.65×** | +3.7 | 0.021 | 20/46 (A-172, NCI-H1573, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.39×** | +3.5 | 0.045 | 11/44 (AsPC-1, PANC-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~57% of this change | **1.55×** | +3.3 | 0.083 | 15/30 (LS 180, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.55×** | +3.2 | 0.083 | 11/46 (J82, KATO III, …) | all doses, flat | cell-cycle shift (explains ~19% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 771.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.248×** | -10.3 | 2e-22 | 41/46 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.408×** | -6.7 | 8e-09 | 38/45 (PANC-1, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.437×** | -6.1 | 1e-07 | 30/45 (J82, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.507×** | -5.0 | 6e-05 | 26/43 (AsPC-1, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~14% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.587×** | -4.0 | 0.009 | 17/39 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.636×** | -3.4 | 0.072 | 11/36 (AsPC-1, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.427×** | -3.3 | 0.072 | 13/41 (COLO 205, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.429×** | -3.3 | 0.072 | 14/39 (NCI-H2030, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.654×** | -3.2 | 0.093 | 18/45 (LoVo, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.444×** | -3.1 | 0.093 | 7/43 (A498, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 771. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 8.46 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.15× (z +12.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.44× (z +8.7) | — |
| [[A-427 (line)]] | wt | 8.42 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.117× (z -8.7) |
| [[A549 (line)]] | wt | 4.04 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0540× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 4.49 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0667× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 3.58 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0654× (z -8.9) |
| [[PANC-1 (line)]] | alt | 7.09 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.149× (z -9.2) |
| [[A498 (line)]] | wt | 7.45 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.40 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.70 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 771), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 19 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS34]] | +0.65 | +0.22 / +0.65 | both halves | 6e-04 |  |
| [[NDUFB10]] | +0.64 | +0.39 / +0.60 | both halves | 5e-05 |  |
| [[PAXX]] ⚠ | +0.62 | +0.25 / +0.63 | both halves | 4e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[RP9]] | +0.62 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[MFSD3]] | +0.62 | +0.41 / +0.67 | both halves | 4e-05 |  |
| [[NME3]] | +0.61 | +0.27 / +0.68 | both halves | 3e-04 |  |
| [[ANTKMT]] | +0.60 | +0.00 / +0.68 | ⚠ one half (not replicated) | 0.009 |  |
| [[CAMKK1]] | +0.60 | +0.32 / +0.52 | both halves | 1e-04 |  |
| [[POLR2I]] | +0.59 | +0.17 / +0.60 | ⚠ one half (not replicated) | 0.001 |  |
| [[THYN1]] | +0.59 | +0.37 / +0.48 | both halves | 8e-05 |  |
| [[LEO1]] | +0.58 | +0.37 / +0.67 | both halves | 9e-05 |  |
| [[TARS2]] | +0.58 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[SCRN2]] | +0.58 | +0.31 / +0.49 | both halves | 2e-04 |  |
| [[SURF2]] | +0.58 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[MIDEAS]] | +0.58 | +0.50 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CERS2]] | -0.63 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[SAP30L-AS1]] | -0.58 | -0.38 / -0.29 | both halves | 2e-04 |  |
| [[SNHG22]] | -0.58 | -0.29 / -0.49 | both halves | 2e-04 |  |
| [[MOB1A]] | -0.56 | -0.29 / -0.60 | both halves | 2e-04 |  |
| [[AVEN]] | -0.56 | -0.30 / -0.40 | both halves | 2e-04 |  |
| [[TMED5]] | -0.55 | -0.44 / -0.60 | both halves | 3e-05 |  |
| [[HEXIM2-AS1]] | -0.55 | -0.26 / -0.28 | both halves | 3e-04 |  |
| [[LENG8-AS1]] | -0.55 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[SLC25A53]] | -0.55 | -0.47 / -0.26 | both halves | 4e-04 |  |
| [[ATXN1L]] | -0.54 | -0.18 / -0.41 | ⚠ not reproduced | 9e-04 |  |
| [[ERAP1]] | -0.54 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[UBE2V1]] | -0.54 | -0.31 / -0.61 | both halves | 2e-04 |  |
| [[MSANTD2]] | -0.54 | -0.39 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FSTL1]] | B | FSTL1 activity lowers NTHL1's level | lines that do not express FSTL1 (21) vs lines expressing it (29) | 1.34× higher at baseline in the lines without FSTL1 | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC8A1, ABI3BP, TFPI2 |
| [[HDAC6]] | B | HDAC6 activity lowers NTHL1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.582). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-47.4, -14.0); signed map (-20.5, -6.1). **Vector** length 66.2, 12.6% of its response variance represented; |z| ≥ 3 in 752 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.3 | +2.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +3.0 | +4.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +2.9 | +3.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.6 | +2.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.6 | +3.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.5 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.4 | +1.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.3 | +2.6 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.1 | -10.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.1 | -6.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.6 | -6.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -2.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -2.6 | -5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -0.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -1.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.7 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -1.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.7 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | nth like DNA glycosylase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:2,039,815-2,047,866 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NTH1, OCTS3 |
| Gene groups (HGNC) | DNA glycosylases; DNA-(apurinic or apyrimidinic site) lyases |
| Hallmark sets | FATTY_ACID_METABOLISM |
| Reactome | 10 pathways, smallest: Diseases of Base Excision Repair; Displacement of DNA glycosylase by APEX1; Cleavage of the damaged pyrimidine |
| Matched by | ensembl_id |

**Function**, from UniProt [P78549](https://www.uniprot.org/uniprotkb/P78549) (Endonuclease III-like protein 1):

> Bifunctional DNA N-glycosylase with associated apurinic/apyrimidinic (AP) lyase function that catalyzes the first step in base excision repair (BER), the primary repair pathway for the repair of oxidative DNA damage. The DNA N-glycosylase activity releases the damaged DNA base from DNA by cleaving the N-glycosidic bond, leaving an AP site. The AP-lyase activity cleaves the phosphodiester bond 3' to the AP site by a beta-elimination. Primarily recognizes and repairs oxidative base damage of …

**Summary**, from NCBI Gene [4913](https://www.ncbi.nlm.nih.gov/gene/4913):

> The protein encoded by this gene is a DNA N-glycosylase of the endonuclease III family. Like a similar protein in E. coli, the encoded protein has DNA glycosylase activity on DNA substrates containing oxidized pyrimidine residues and has apurinic/apyrimidinic lyase activity. [provided by RefSeq, Oct 2008]

**Accessions** — [HGNC:8028](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8028) · Entrez [4913](https://www.ncbi.nlm.nih.gov/gene/4913) · UniProt [P78549](https://www.uniprot.org/uniprotkb/P78549) · Ensembl [ENSG00000065057](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000065057)

## Data

Gene col 771: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 771); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 771, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 771]; `tensor/DDL_lfc|DDL_z.npy` [771]; `embed/gene_vectors.npy` [771]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 771 or target_col == 771). Every well: [[NTHL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NTHL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
