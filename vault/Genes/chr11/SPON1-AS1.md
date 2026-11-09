---
symbol: "SPON1-AS1"
type: "gene"
col: 14871
ensembl_id: "ENSG00000254418"
name: "SPON1 antisense RNA 1"
location: "11p15.2"
module: 47
arm: "+"
pooled_cpm: 9.61
n_lines_expressing: 48
n_dd_up: 23
n_dd_down: 1
n_dd_up_clean: 20
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# SPON1-AS1

*SPON1 antisense RNA 1* — 11p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.03× (z +11.6, q 4e-28, up in 32 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Pralsetinib (drug)]] 5 µM: 0.532× (z -3.8, q 0.080, down in 12 of 37 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (LOX-IMVI 0.0867×, HEC-1-A 0.166×, SW480 0.212×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 1 line (A-427 0.0730×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.117×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change); [[Ipatasertib (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.0695×); [[Cinacalcet (drug)]] 0.5 µM in 1 line (BT-474 0.0738×); [[Elagolix sodium (drug)]] 0.5 µM in 1 line (SNU-1 0.0704×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MCF2]] (+0.73, fdr 1e-05), [[PSMD6-AS1]] (+0.72, fdr 7e-06), [[LINC01191]] (+0.71, fdr 7e-06); moves opposite to [[THYN1]] (-0.70, fdr 1e-05), [[ATG4C]] (-0.68, fdr 5e-05), [[ALAD]] (-0.68, fdr 3e-05).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14871.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.03×** | +11.6 | 4e-28 | 32/41 (A-172, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.84×** | +9.9 | 9e-21 | 26/42 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.75×** | +6.5 | 2e-08 | 26/45 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.17× | +6.3 | 5e-08 | 12/46 (LOX-IMVI, NCI-H1792, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.64×** | +5.7 | 1e-06 | 23/44 (LoVo, A-172, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.64×** | +5.7 | 1e-06 | 27/44 (NCI-H2030, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +5.2 | 2e-05 | 18/39 (NCI-H460, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.35×** | +4.9 | 7e-05 | 18/43 (NCI-H23, HT-29, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.52×** | +4.8 | 9e-05 | 18/40 (MIA PaCa-2, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.51×** | +4.7 | 1e-04 | 16/42 (NCI-H460, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.46×** | +4.2 | 0.002 | 18/44 (HT-29, NCI-H23, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.43×** | +4.1 | 0.002 | 14/45 (NCI-H2030, HepG2/C3A, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +3.9 | 0.003 | 12/41 (KATO III, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.38×** | +3.7 | 0.009 | 18/42 (NCI-H2347, NCI-H460, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.82×** | +3.6 | 0.011 | 5/44 (LoVo, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.5 | 0.017 | 12/45 (A-172, A-427, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.35×** | +3.4 | 0.019 | 12/45 (AsPC-1, HS-578T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14871.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (LOX-IMVI 0.0867×, HEC-1-A 0.166×, SW480 0.212×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 1 line (A-427 0.0730×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.117×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change); [[Ipatasertib (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.0695×); [[Cinacalcet (drug)]] 0.5 µM in 1 line (BT-474 0.0738×); [[Elagolix sodium (drug)]] 0.5 µM in 1 line (SNU-1 0.0704×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pralsetinib (drug)]] 5 µM |  | **0.532×** | -3.8 | 0.080 | 12/37 (C-33 A, NCI-H1792, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14871. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 18.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0867× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 11.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.206× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 9.65 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.98× (z +9.6) | — |
| [[A-427 (line)]] | wt | 12.3 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0730× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 8.98 | 0 | 1 | — | [[Cinacalcet (drug)]] 0.5 µM 0.0738× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 16.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.166× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 16.0 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.122× (z -8.8) ⚠ toxic; unreliable plate only |
| [[LoVo (line)]] | wt | 9.28 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +12.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 10.9 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.5 µM 0.0695× (z -10.4) |
| [[PANC-1 (line)]] | alt | 7.31 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +10.1) | — |
| [[SNU-1 (line)]] | wt | 11.1 | 0 | 1 | — | [[Elagolix sodium (drug)]] 0.5 µM 0.0704× (z -9.3) |
| [[SW480 (line)]] | alt | 7.83 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.212× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.47 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.20 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.66 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.11 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.92 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.740 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.62 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14871), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCF2]] | +0.73 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[PSMD6-AS1]] | +0.72 | +0.68 / +0.58 | both halves | 7e-06 | same gene group |
| [[LINC01191]] | +0.71 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[PSMD6-AS2]] | +0.69 | +0.65 / +0.55 | both halves | 1e-05 | same gene group |
| [[ANKDD1B]] | +0.67 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[QRICH2]] | +0.67 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[CCDC17]] | +0.66 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[TMEM236]] | +0.65 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[SLC2A9]] | +0.65 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[MYH3]] | +0.65 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[SMIM15-AS1]] | +0.64 | +0.55 / +0.53 | both halves | 1e-05 | same gene group |
| [[PPP1R12A-AS2]] | +0.64 | +0.56 / +0.47 | both halves | 2e-05 | same gene group |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THYN1]] | -0.70 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[ATG4C]] | -0.68 | -0.65 / -0.40 | both halves | 5e-05 |  |
| [[ALAD]] | -0.68 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[POT1]] | -0.67 | -0.61 / -0.46 | both halves | 3e-05 |  |
| [[ORC4]] | -0.66 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[NDUFA12]] | -0.65 | -0.51 / -0.46 | both halves | 2e-05 |  |
| [[SKIC3]] | -0.64 | -0.65 / -0.36 | both halves | 1e-04 |  |
| [[SCRN2]] | -0.64 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[RAB3A]] | -0.64 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[PIP4P2]] | -0.63 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[METTL17]] | -0.62 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[RFC1]] | -0.61 | -0.57 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SPON1-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[DYSF]] | B | DYSF activity raises SPON1-AS1's level | lines that do not express DYSF (11) vs lines expressing it (39) | 1.39× lower at baseline in the lines without DYSF | 0.085 | ⚠ within organs, on part of the lines; also absent: ISM2, IRX3, DNAAF9; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.458). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (7.0, 7.0); signed map (18.8, 1.1). **Vector** length 75.3, 14.1% of its response variance represented; |z| ≥ 3 in 829 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +11.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +5.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +3.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.2 | +4.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.2 | +3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.1 | +4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +3.5 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -0.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -0.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.8 | -1.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | +1.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -1.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | +0.6 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.7 | -1.4 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.6 | -2.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.5 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | SPON1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 11p15.2 — chr11:14,262,846-14,273,691 (-) |
| Ensembl biotype | lncRNA |
| Also known as | RP11-21, L19.1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53117](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53117) · Entrez [109729138](https://www.ncbi.nlm.nih.gov/gene/109729138) · Ensembl [ENSG00000254418](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000254418)

## Data

Gene col 14871: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14871); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14871, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14871]; `tensor/DDL_lfc|DDL_z.npy` [14871]; `embed/gene_vectors.npy` [14871]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14871 or target_col == 14871). Every well: [[SPON1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPON1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
