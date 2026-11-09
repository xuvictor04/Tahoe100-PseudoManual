---
symbol: "CMAHP"
type: "gene"
col: 9646
ensembl_id: "ENSG00000168405"
name: "cytidine monophospho-N-acetylneuraminic acid hydroxylase, pseudogene"
location: "6p22.3"
module: 21
arm: "+"
pooled_cpm: 7.53
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 3
n_dd_up_clean: 14
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# CMAHP

*cytidine monophospho-N-acetylneuraminic acid hydroxylase, pseudogene* — 6p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.55× (z +20.0, q 0e+00, up in 37 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.874× (z -6.9, q 3e-09, down in 15 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.757× (z -4.2, q 0.009, down in 14 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC27A6]] (+0.70, fdr 2e-05), [[C2CD5-AS1]] (+0.68, fdr 2e-05), [[HRG-AS1]] (+0.68, fdr 1e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9646.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.55×** | +20.0 | 0e+00 | 37/44 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.52×** | +12.9 | 1e-35 | 14/21 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.33×** | +12.8 | 5e-35 | 24/32 (KATO III, SW480, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.35×** | +12.4 | 3e-33 | 10/14 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.62×** | +7.3 | 4e-11 | 24/47 (A549, A-172, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.55×** | +6.6 | 3e-09 | 14/46 (J82, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +6.5 | 5e-09 | 15/47 (J82, SW480, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +5.2 | 1e-05 | 14/40 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +5.1 | 2e-05 | 15/47 (HEC-1-A, CFPAC-1, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +4.7 | 1e-04 | 14/42 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~6% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +4.4 | 7e-04 | 11/38 (NCI-H2030, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.32×** | +4.2 | 0.001 | 12/41 (A498, A-172, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib (drug)]] 0.05 µM |  | **1.34×** | +4.2 | 0.001 | 8/45 (HepG2/C3A, NCI-H23, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 1.19× | +3.7 | 0.009 | 5/46 (HS-578T, RPMI-7951, …) | rises with dose | position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.26×** | +3.5 | 0.016 | 10/43 (NCI-H1792, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.038 | 5/45 (C32, HepG2/C3A, …) | inconsistent across doses | position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.040 | 4/44 (Hs 766T, SNU-423, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.22×** | +3.0 | 0.073 | 2/46 (HT-29, H4) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.32×** | +3.0 | 0.073 | 6/41 (PANC-1, SNU-423, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **1.22×** | +3.0 | 0.077 | 10/43 (A-427, A-172, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9646.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.874× | -6.9 | 3e-09 | 15/48 (NCI-H2347, PANC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.757×** | -4.2 | 0.009 | 14/46 (SNU-423, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~1% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.782×** | -3.7 | 0.046 | 10/46 (C-33 A, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Roxadustat (drug)]] 5 µM |  | **0.789×** | -3.4 | 0.094 | 4/44 (RKO, A549, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.794× | -3.2 | 0.16 | 11/42 (BT-474, A-172, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9646. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 5.97 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.54× (z +9.0) | — |
| [[A549 (line)]] | wt | 5.70 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.0896× (z -8.7) |
| [[BT-474 (line)]] | alt | 14.2 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0895× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 9.59 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.61× (z +12.8) | — |
| [[CHP-212 (line)]] | wt | 29.7 | 0 | 1 | — | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM 0.0671× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 6.27 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.95× (z +10.1) | — |
| [[KATO III (line)]] | alt | 9.13 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.85× (z +11.1) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 8.85 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 6.48× (z +10.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 5.65 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.95× (z +10.8) | — |
| [[SW480 (line)]] | alt | 6.50 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.02× (z +11.9) | — |
| [[A-172 (line)]] | wt | 5.23 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.36 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.29 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.15 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.20 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.94 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.80 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.48 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9646), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC27A6]] | +0.70 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[C2CD5-AS1]] | +0.68 | +0.47 / +0.69 | both halves | 2e-05 |  |
| [[HRG-AS1]] | +0.68 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[ENTPD1]] | +0.64 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[SLC26A5]] | +0.64 | +0.48 / +0.70 | both halves | 2e-05 |  |
| [[ZNF451-AS1]] | +0.63 | +0.41 / +0.64 | both halves | 4e-05 |  |
| [[CHMP3-AS1]] | +0.63 | +0.40 / +0.61 | both halves | 5e-05 |  |
| [[C12orf40]] | +0.63 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[PTPRT]] | +0.62 | +0.46 / +0.65 | both halves | 3e-05 |  |
| [[GEMIN7-AS1]] | +0.62 | +0.40 / +0.67 | both halves | 5e-05 |  |
| [[FLJ40194]] | +0.62 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[TICAM2-AS1]] | +0.62 | +0.49 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CMAHP's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HOXA-AS2]] | C | HOXA-AS2 activity lowers CMAHP's level | lines that do not express HOXA-AS2 (3) vs lines expressing it (47) | 2.40× higher at baseline in the lines without HOXA-AS2 | 0.004 | ⚠ few lines (3 vs 47); across organs; also absent: HFE, COTL1, ACCS; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.649). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.8, 26.4); signed map (33.2, 3.9). **Vector** length 57.0, 7.61% of its response variance represented; |z| ≥ 3 in 866 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.4 | +20.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.5 | +12.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.1 | +12.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.8 | +12.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +6.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +5.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.0 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +3.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.5 | +2.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.3 | -4.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.2 | -6.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -1.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.6 | -1.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | +0.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -1.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | +0.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.2 | -1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.2 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | cytidine monophospho-N-acetylneuraminic acid hydroxylase, pseudogene |
| Locus type | pseudogene |
| Location | 6p22.3 — chr6:25,081,862-25,138,081 (-) |
| Ensembl biotype | transcribed_unitary_pseudogene |
| Also known as | ; previously CMAH |
| Gene groups (HGNC) | Metallo-beta-lactamase fold containing family; Unitary pseudogenes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y471](https://www.uniprot.org/uniprotkb/Q9Y471) (Inactive cytidine monophosphate-N-acetylneuraminic acid hydroxylase):

> Sialic acids are components of carbohydrate chains of glycoconjugates and are involved in cell-cell recognition and cell-pathogen interactions. That protein has no CMP-N-acetylneuraminate monooxygenase activity and is not able to convert CMP-N-acetylneuraminic acid (CMP-Neu5Ac) into its hydroxylated derivative CMP-N-glycolylneuraminic acid (CMP-Neu5Gc), a sialic acid abundantly expressed at the surface of many cells in vertebrates. However, it may play a role in Wnt signaling.

**Summary**, from NCBI Gene [8418](https://www.ncbi.nlm.nih.gov/gene/8418):

> Sialic acids are terminal components of the carbohydrate chains of glycoconjugates involved in ligand-receptor, cell-cell, and cell-pathogen interactions. The two most common forms of sialic acid found in mammalian cells are N-acetylneuraminic acid (Neu5Ac) and its hydroxylated derivative, N-glycolylneuraminic acid (Neu5Gc). Studies of sialic acid distribution show that Neu5Gc is not detectable in normal human tissues although it was an abundant sialic acid in other mammals. Neu5Gc is, in …

**Accessions** — [HGNC:2098](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2098) · Entrez [8418](https://www.ncbi.nlm.nih.gov/gene/8418) · UniProt [Q9Y471](https://www.uniprot.org/uniprotkb/Q9Y471) · Ensembl [ENSG00000168405](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168405)

## Data

Gene col 9646: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9646); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9646, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9646]; `tensor/DDL_lfc|DDL_z.npy` [9646]; `embed/gene_vectors.npy` [9646]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9646 or target_col == 9646). Every well: [[CMAHP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CMAHP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
