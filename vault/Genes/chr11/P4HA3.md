---
symbol: "P4HA3"
type: "gene"
col: 7370
ensembl_id: "ENSG00000149380"
name: "prolyl 4-hydroxylase subunit alpha 3"
location: "11q13.4"
module: 19
arm: "+"
pooled_cpm: 8.74
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# P4HA3

*prolyl 4-hydroxylase subunit alpha 3* — 11q13.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.21× (z +13.4, q 2e-38, up in 30 of 41 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A549 0.266×, NCI-H460 0.330×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A549 0.145×; ⚠ cell-cycle shift, explains ~11% of this change); [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0570×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A549 0.166×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AADACL2-AS1]] (+0.68, fdr 7e-06), [[CACNG6]] (+0.63, fdr 1e-05), [[RBFOX1]] (+0.63, fdr 7e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[BMPER]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7370.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.21×** | +13.4 | 2e-38 | 30/41 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.71×** | +12.0 | 1e-30 | 19/28 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.28×** | +9.5 | 3e-19 | 9/14 (J82, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.94×** | +7.3 | 5e-11 | 11/19 (J82, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +6.7 | 3e-09 | 19/39 (HEC-1-A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +5.2 | 1e-05 | 16/46 (PANC-1, A-427, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +5.2 | 2e-05 | 17/45 (HEC-1-A, HT-29, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.50×** | +4.8 | 9e-05 | 18/47 (PANC-1, A-427, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.46×** | +4.6 | 3e-04 | 9/35 (HOP62, A-172, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | **1.38×** | +3.9 | 0.005 | 10/44 (J82, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.26×** | +3.9 | 0.005 | 15/39 (LoVo, A-172, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.9 | 0.005 | 4/35 (A-427, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +3.7 | 0.008 | 12/46 (Hs 766T, NCI-H1792, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.37×** | +3.6 | 0.011 | 5/42 (A-427, NCI-H1573, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +3.5 | 0.016 | 7/47 (A498, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.31×** | +3.2 | 0.037 | 6/46 (J82, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **1.30×** | +3.2 | 0.048 | 7/39 (J82, RPMI-7951, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.20× | +3.0 | 0.062 | 8/47 (A-172, HOP62, …) | top dose only |  |
| [[Verteporfin (drug)]] 0.5 µM |  | **1.27×** | +2.9 | 0.088 | 0/46 | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.27×** | +2.9 | 0.088 | 6/44 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7370.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A549 0.266×, NCI-H460 0.330×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A549 0.145×; ⚠ cell-cycle shift, explains ~11% of this change); [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0570×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A549 0.166×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.824× | -3.3 | 0.36 | 11/47 (A-427, NCI-H1792, …) | all doses, flat | position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.827× | -3.1 | 0.36 | 7/47 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.761× | -3.1 | 0.36 | 6/47 (LS 180, HepG2/C3A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7370. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 60.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -14.8) ⚠ cell-cycle shift, explains ~11% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -10.2) |
| [[BT-474 (line)]] | alt | 5.67 | 0 | 1 | — | [[Crizotinib (hydrochloride) (drug)]] 0.5 µM 0.0806× (z -8.5) |
| [[LoVo (line)]] | wt | 3.98 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.86× (z +8.9) ⚠ cell-cycle shift, explains ~11% of this change | — |
| [[LOX-IMVI (line)]] | wt | 5.13 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM 0.0570× (z -11.8) |
| [[MIA PaCa-2 (line)]] | alt | 4.63 | 0 | 1 | — | [[Thymol (drug)]] 0.05 µM 0.102× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 31.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 4.32 | 0 | 1 | — | [[Pentoxifylline (drug)]] 0.5 µM 0.0613× (z -8.8) |
| [[A-172 (line)]] | wt | 6.92 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.42 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.63 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.35 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.44 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.45 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.45 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.83 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7370), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AADACL2-AS1]] | +0.68 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[CACNG6]] | +0.63 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[RBFOX1]] | +0.63 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[SPTBN1-AS2]] | +0.62 | +0.65 / +0.57 | both halves | 9e-06 |  |
| [[NOS1]] | +0.60 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[ANO3]] | +0.60 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[SCUBE1]] | +0.59 | +0.51 / +0.70 | both halves | 1e-05 | pathway: Extracellular matrix organization |
| [[FILIP1]] | +0.59 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[PLAC4]] | +0.59 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[UNC5D]] | +0.59 | +0.46 / +0.68 | both halves | 3e-05 |  |
| [[C12orf40]] | +0.58 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[LINC02755]] | +0.58 | +0.48 / +0.64 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BMPER]] | B | BMPER activity raises P4HA3's level | lines that do not express BMPER (21) vs lines expressing it (29) | 1.71× lower at baseline in the lines without BMPER | 0.027 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R |
| [[SPOCK1]] | B | SPOCK1 activity raises P4HA3's level | lines that do not express SPOCK1 (29) vs lines expressing it (21) | 1.90× lower at baseline in the lines without SPOCK1 | 0.032 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[NCKAP5-AS2]] | B | NCKAP5-AS2 activity raises P4HA3's level | lines that do not express NCKAP5-AS2 (31) vs lines expressing it (19) | 1.66× lower at baseline in the lines without NCKAP5-AS2 | 0.061 | ⚠ within organs, on part of the lines; also absent: MEG3, PDGFRB, UNC5D |
| [[TRPA1]] | B | TRPA1 activity raises P4HA3's level | lines that do not express TRPA1 (31) vs lines expressing it (19) | 1.79× lower at baseline in the lines without TRPA1 | 0.067 | ⚠ within organs, on part of the lines; also absent: ITGA4, DOCK10, INSYN2B |
| [[LINC00922]] | B | LINC00922 activity raises P4HA3's level | lines that do not express LINC00922 (9) vs lines expressing it (41) | 1.33× lower at baseline in the lines without LINC00922 | 0.089 | ⚠ within organs, on part of the lines; also absent: MGC4859, ENSG00000250149, LINC01811; maybe low, not absent |
| [[PPEF1]] | C | PPEF1's natural level weakens P4HA3's drug response | PPEF1's natural level across 43 lines (lineage-adjusted; a glimpse) | r -0.69, reverse -0.29; direction clear | 0.048 | ⚠ tissue can mimic it; precision caveat |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.530). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (18.7, 25.5); signed map (28.4, 14.7). **Vector** length 60.8, 8.94% of its response variance represented; |z| ≥ 3 in 826 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.2 | +12.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.1 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.9 | +7.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +13.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +3.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.0 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +0.6 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.6 | -2.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.5 | -1.0 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -2.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.0 | -2.6 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.7 | -1.1 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.6 | -1.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.6 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | prolyl 4-hydroxylase subunit alpha 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.4 — chr11:74,235,801-74,311,640 (-) |
| Ensembl biotype | protein_coding |
| Also known as | C-P4Halpha(III) |
| Gene groups (HGNC) | Iron (II) and 2-oxoglutarate dependent oxygenases; Prolyl 4-hydroxylase subunits |
| Reactome | 7 pathways, smallest: Maturation of DENV proteins; Collagen biosynthesis and modifying enzymes; Collagen formation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z4N8](https://www.uniprot.org/uniprotkb/Q7Z4N8) (Prolyl 4-hydroxylase subunit alpha-3):

> Catalyzes the post-translational formation of 4-hydroxyproline in -Xaa-Pro-Gly- sequences in collagens and other proteins.

**Summary**, from NCBI Gene [283208](https://www.ncbi.nlm.nih.gov/gene/283208):

> This gene encodes a component of prolyl 4-hydroxylase, a key enzyme in collagen synthesis composed of two identical alpha subunits and two beta subunits. The encoded protein is one of several different types of alpha subunits and provides the major part of the catalytic site of the active enzyme. In collagen and related proteins, prolyl 4-hydroxylase catalyzes the formation of 4-hydroxyproline that is essential to the proper three-dimensional folding of newly synthesized procollagen chains. …

**Accessions** — [HGNC:30135](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30135) · Entrez [283208](https://www.ncbi.nlm.nih.gov/gene/283208) · UniProt [Q7Z4N8](https://www.uniprot.org/uniprotkb/Q7Z4N8) · Ensembl [ENSG00000149380](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149380)

## Data

Gene col 7370: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7370); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7370, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7370]; `tensor/DDL_lfc|DDL_z.npy` [7370]; `embed/gene_vectors.npy` [7370]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7370 or target_col == 7370). Every well: [[P4HA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/P4HA3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
