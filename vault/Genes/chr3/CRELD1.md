---
symbol: "CRELD1"
type: "gene"
col: 8760
ensembl_id: "ENSG00000163703"
name: "CRELD disulfide isomerase 1"
location: "3p25.3"
module: 42
arm: "+"
pooled_cpm: 14.39
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 14
n_dd_up_clean: 5
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# CRELD1

*CRELD disulfide isomerase 1* — 3p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.50× (z +9.1, q 8e-17, up in 33 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.555× (z -9.3, q 1e-17, down in 37 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSP90B1]] (+0.75, fdr 7e-06), [[HSPA5]] (+0.73, fdr 7e-06), [[PDIA4]] (+0.72, fdr 7e-06); moves opposite to [[AASDHPPT]] (-0.61, fdr 8e-06), [[PAK1IP1]] (-0.60, fdr 1e-05), [[ADO]] (-0.60, fdr 8e-06).
> It is in [[Module 042]], a single-armed module (UPR ER).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8760.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +9.1 | 8e-17 | 33/46 (SW1417, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.57×** | +7.1 | 3e-10 | 30/48 (NCI-H1792, A-172, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +6.1 | 2e-07 | 11/27 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.46×** | +6.0 | 3e-07 | 25/48 (NCI-H1792, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +5.3 | 1e-05 | 15/47 (HT-29, HOP62, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.33×** | +4.2 | 0.002 | 15/46 (SNU-1, SW48, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.31×** | +4.2 | 0.002 | 14/36 (C32, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.27×** | +3.7 | 0.014 | 10/47 (HEC-1-A, SK-MEL-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8760.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.555×** | -9.3 | 1e-17 | 37/47 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.545×** | -9.2 | 1e-17 | 34/47 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.614×** | -7.7 | 3e-12 | 28/48 (PANC-1, HOP62, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.668×** | -6.3 | 3e-08 | 20/46 (NCI-H2347, HOP62, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.714×** | -5.3 | 1e-05 | 19/47 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.788×** | -5.3 | 1e-05 | 25/47 (KATO III, RKO, …) | all doses, flat | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.633×** | -3.8 | 0.014 | 12/45 (CHP-212, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.780×** | -3.6 | 0.020 | 17/45 (SW 900, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **0.646×** | -3.6 | 0.020 | 16/48 (SW 900, LS 180, …) | all doses, flat | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.799×** | -3.5 | 0.024 | 9/47 (HCT15, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.810×** | -3.3 | 0.047 | 12/47 (NCI-H2030, Hs 766T, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.674×** | -3.2 | 0.056 | 10/47 (NCI-H460, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.816×** | -3.2 | 0.056 | 10/48 (HCT15, A-172, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.816×** | -3.2 | 0.056 | 6/47 (SNU-423, HOP62, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.867× | -3.2 | 0.057 | 8/48 (C32, NCI-H460, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8760. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 37.0 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.328× (z -10.3) |
| [[KATO III (line)]] | alt | 19.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 6.06 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0666× (z -11.3) |
| [[C32 (line)]] | wt | 16.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.03× (z +9.2) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 11.8 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0978× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 18.5 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.0938× (z -10.3) |
| [[HCT15 (line)]] | alt | 36.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -8.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 16.1 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0740× (z -11.6) |
| [[MIA PaCa-2 (line)]] | alt | 9.54 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.108× (z -11.2) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 18.0 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.237× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 18.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.270× (z -9.8) |
| [[RKO (line)]] | wt | 16.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -9.6) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SW 900 (line)]] | alt | 9.48 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0662× (z -11.0) |
| [[SW48 (line)]] | wt | 18.7 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.120× (z -8.7) |
| [[A-172 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.34 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.33 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.69 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.81 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.81 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8760), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSP90B1]] | +0.75 | +0.71 / +0.75 | both halves | 7e-06 |  |
| [[HSPA5]] | +0.73 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[PDIA4]] | +0.72 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[LMAN1]] | +0.70 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[CDC26]] | +0.70 | +0.59 / +0.76 | both halves | 7e-06 |  |
| [[COPA]] | +0.69 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[C12orf73]] | +0.67 | +0.49 / +0.76 | both halves | 1e-05 |  |
| [[DNAJC3]] | +0.67 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[HYOU1]] | +0.67 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[SURF4]] | +0.66 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[SEL1L]] | +0.66 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[KDELR1]] | +0.66 | +0.59 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AASDHPPT]] | -0.61 | -0.58 / -0.58 | both halves | 8e-06 |  |
| [[PAK1IP1]] | -0.60 | -0.56 / -0.65 | both halves | 1e-05 |  |
| [[ADO]] | -0.60 | -0.57 / -0.58 | both halves | 8e-06 |  |
| [[TIGD2]] | -0.59 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[DDX20]] | -0.59 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[RIF1]] | -0.58 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[ERCC4]] | -0.58 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[TADA2A]] | -0.57 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[COA7]] | -0.57 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[RRS1]] | -0.57 | -0.57 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.704). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.9, -30.4); signed map (-53.9, 7.3). **Vector** length 80.2, 14.2% of its response variance represented; |z| ≥ 3 in 921 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *UPR ER* (control, mean cos +0.64 to 11); *Maturation of DENV proteins* (reactome, mean cos +0.55 to 11); *Dengue Virus Genome Translation and Replication* (reactome, mean cos +0.55 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +9.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +6.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +5.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +4.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.4 | +2.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.0 | +2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.6 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.3 | +2.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -7.1 | -9.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.5 | -9.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.9 | -7.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.6 | -6.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.5 | -5.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.6 | -2.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.5 | -3.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.3 | -3.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.2 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | CRELD disulfide isomerase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.3 — chr3:9,933,793-9,945,413 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CIRRIN; previously AVSD2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96HD1](https://www.uniprot.org/uniprotkb/Q96HD1) (Protein disulfide isomerase CRELD1):

> Protein disulfide isomerase (By similarity). Promotes the localization of acetylcholine receptors (AChRs) to the plasma membrane (By similarity).

**Summary**, from NCBI Gene [78987](https://www.ncbi.nlm.nih.gov/gene/78987):

> This gene encodes a member of a subfamily of epidermal growth factor-related proteins. The encoded protein is characterized by a cysteine-rich with epidermal growth factor-like domain. This protein may function as a cell adhesion molecule. Mutations in this gene are the cause of atrioventricular septal defect. Alternate splicing results in multiple transcript variants.[provided by RefSeq, Apr 2010]

**Accessions** — [HGNC:14630](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14630) · Entrez [78987](https://www.ncbi.nlm.nih.gov/gene/78987) · UniProt [Q96HD1](https://www.uniprot.org/uniprotkb/Q96HD1) · Ensembl [ENSG00000163703](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163703)

## Data

Gene col 8760: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8760); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8760, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8760]; `tensor/DDL_lfc|DDL_z.npy` [8760]; `embed/gene_vectors.npy` [8760]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8760 or target_col == 8760). Every well: [[CRELD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRELD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
