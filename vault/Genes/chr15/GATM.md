---
symbol: "GATM"
type: "gene"
col: 10159
ensembl_id: "ENSG00000171766"
name: "glycine amidinotransferase"
location: "15q21.1"
module: 14
arm: "+"
pooled_cpm: 3.49
n_lines_expressing: 43
n_dd_up: 31
n_dd_down: 7
n_dd_up_clean: 23
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# GATM

*glycine amidinotransferase* — 15q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.33× (z +23.9, q 0e+00, up in 23 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.619× (z -4.9, q 6e-04, down in 13 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02605]] (+0.69, fdr 7e-06), [[TRAF1]] (+0.68, fdr 7e-06), [[PLAU]] (+0.64, fdr 1e-05); moves opposite to [[TYW1]] (-0.50, fdr 4e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[SLC43A3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10159.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.33×** | +23.9 | 0e+00 | 23/26 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.58×** | +12.4 | 1e-32 | 3/5 (KATO III, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.32×** | +12.0 | 6e-31 | 15/26 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.90×** | +10.7 | 9e-25 | 4/9 (KATO III, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.11×** | +10.6 | 5e-24 | 5/7 (KATO III, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.71×** | +10.0 | 9e-22 | 21/37 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.50×** | +8.9 | 6e-17 | 12/24 (HOP62, A498, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.30×** | +8.4 | 4e-15 | 17/36 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.78×** | +8.2 | 1e-14 | 17/35 (PANC-1, NCI-H2347, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.78×** | +8.2 | 1e-14 | 10/37 (KATO III, NCI-H1573, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.30×** | +8.1 | 4e-14 | 13/29 (HOP62, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.99×** | +6.9 | 2e-10 | 13/23 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.95×** | +6.7 | 9e-10 | 18/36 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +6.0 | 7e-08 | 5/14 (CFPAC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Amsacrine (drug)]] 5 µM |  | **1.44×** | +5.1 | 1e-05 | 6/35 (A-172, A498, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.61×** | +4.8 | 6e-05 | 13/37 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.60×** | +4.7 | 9e-05 | 10/36 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.57×** | +4.6 | 2e-04 | 12/29 (CFPAC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.60×** | +4.6 | 2e-04 | 12/35 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10159.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.619×** | -4.9 | 6e-04 | 13/37 (NCI-H23, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.673×** | -4.0 | 0.015 | 10/34 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 5 µM |  | **0.688×** | -3.8 | 0.026 | 6/37 (NCI-H1573, NCI-H1792, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.699×** | -3.7 | 0.037 | 13/35 (SNU-1, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.707×** | -3.5 | 0.044 | 1/37 (HT-29) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.719×** | -3.4 | 0.070 | 5/36 (NCI-H1573, LS 180, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.713×** | -3.3 | 0.072 | 13/35 (A498, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10159. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 28.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 8.95× (z +10.7) ⚠ toxic; transcription drop | [[5-Azacytidine (drug)]] 5 µM 0.186× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 18.5 | 1 | 2 | [[Homoharringtonine (drug)]] 0.05 µM 5.19× (z +8.6) | [[Ixazomib citrate (drug)]] 5 µM 0.116× (z -11.3) |
| [[PANC-1 (line)]] | alt | 2.10 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 16.5× (z +10.1) | — |
| [[A-172 (line)]] | wt | 3.20 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.41× (z +9.0) | — |
| [[A-427 (line)]] | wt | 9.70 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.139× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~42% of this change |
| [[A498 (line)]] | wt | 1.33 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.9× (z +9.3) | — |
| [[HOP62 (line)]] | alt | 2.76 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.55× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 17.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0813× (z -10.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 6.68 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.105× (z -9.4) ⚠ transcription drop |
| [[A549 (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.914 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.475 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.800 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.658 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.99 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.749 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.691 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.82 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.802 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.737 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10159), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02605]] | +0.69 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[TRAF1]] | +0.68 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[PLAU]] | +0.64 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[NKX3-1]] | +0.64 | +0.71 / +0.53 | both halves | 1e-05 |  |
| [[ADORA2A]] | +0.64 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[IFNGR2]] | +0.64 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[CYB5R2]] | +0.63 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[IL1A]] | +0.63 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[DSE]] | +0.62 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[NEURL3]] | +0.62 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[CPAMD8]] | +0.62 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[TNFRSF9]] | +0.62 | +0.60 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TYW1]] | -0.50 | -0.51 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GATM's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 5.6% of all compounds | 0.006 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[NR3C1]] | B | NR3C1 activity lowers GATM's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 2.0% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds |
| [[CACNG2]] | B | CACNG2 activity lowers GATM's level | lines that do not express CACNG2 (9) vs lines expressing it (41) | 2.47× higher at baseline in the lines without CACNG2 | 0.027 | ⚠ within organs, on part of the lines; also absent: FRMD3, NFATC2, ENSG00000285082; maybe low, not absent |
| [[NKX3-1]] | B | NKX3-1 activity raises GATM's level | lines that do not express NKX3-1 (13) vs lines expressing it (37) | 1.72× lower at baseline in the lines without NKX3-1 | 0.067 | ⚠ within organs, on part of the lines; also absent: OSMR, IL1R1, OSMR-DT; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC43A3]] | B | GATM activity lowers SLC43A3's level | lines that do not express GATM (7) vs lines expressing it (43) | 2.65× higher at baseline in the lines without GATM | 0.090 | ⚠ within organs, on part of the lines; also absent: CTSH, KIAA1522; maybe low, not absent |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.652). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.6, 2.1); signed map (41.4, 10.9). **Vector** length 56.1, 8.94% of its response variance represented; |z| ≥ 3 in 992 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +10.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +23.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +12.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +10.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.5 | +12.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +8.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +4.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.5 | +5.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.5 | +2.2 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -2.1 | -4.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.0 | -1.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -2.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.8 | -3.8 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.7 | -3.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.6 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | glycine amidinotransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.1 — chr15:45,361,124-45,402,327 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AGAT |
| Reactome | 2 pathways, smallest: Creatine metabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P50440](https://www.uniprot.org/uniprotkb/P50440) (Glycine amidinotransferase, mitochondrial):

> Transamidinase that catalyzes the transfer of the amidino group of L-arginine onto the amino moiety of acceptor metabolites such as glycine, beta-alanine, gamma-aminobutyric acid (GABA) and taurine yielding the corresponding guanidine derivatives. Catalyzes the rate-limiting step of creatine biosynthesis, namely the transfer of the amidino group from L-arginine to glycine to generate guanidinoacetate, which is then methylated by GAMT to form creatine. Provides creatine as a source for ATP …

**Summary**, from NCBI Gene [2628](https://www.ncbi.nlm.nih.gov/gene/2628):

> This gene encodes a mitochondrial enzyme that belongs to the amidinotransferase family. This enzyme is involved in creatine biosynthesis, whereby it catalyzes the transfer of a guanido group from L-arginine to glycine, resulting in guanidinoacetic acid, the immediate precursor of creatine. Mutations in this gene cause arginine:glycine amidinotransferase deficiency, an inborn error of creatine synthesis characterized by cognitive disability, language impairment, and behavioral disorders. …

**Accessions** — [HGNC:4175](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4175) · Entrez [2628](https://www.ncbi.nlm.nih.gov/gene/2628) · UniProt [P50440](https://www.uniprot.org/uniprotkb/P50440) · Ensembl [ENSG00000171766](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171766)

## Data

Gene col 10159: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10159); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10159, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10159]; `tensor/DDL_lfc|DDL_z.npy` [10159]; `embed/gene_vectors.npy` [10159]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10159 or target_col == 10159). Every well: [[GATM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GATM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
