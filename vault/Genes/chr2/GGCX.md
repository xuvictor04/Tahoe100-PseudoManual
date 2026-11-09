---
symbol: "GGCX"
type: "gene"
col: 3683
ensembl_id: "ENSG00000115486"
name: "gamma-glutamyl carboxylase"
location: "2p11.2"
module: 42
arm: "+"
pooled_cpm: 18.39
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 6
n_dd_up_clean: 6
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# GGCX

*gamma-glutamyl carboxylase* — 2p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.30× (z +17.6, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.663× (z -8.7, q 2e-15, down in 25 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAR1A]] (+0.75, fdr 7e-06), [[CYB561D2]] (+0.72, fdr 7e-06), [[PDIA4]] (+0.72, fdr 1e-05); moves opposite to [[CCDC122]] (-0.62, fdr 8e-05), [[INO80D]] (-0.61, fdr 5e-05), [[PBDC1]] (-0.61, fdr 4e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3683.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.30×** | +17.6 | 0e+00 | 45/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.04×** | +15.1 | 0e+00 | 44/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.91×** | +13.7 | 2e-40 | 42/48 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +8.9 | 5e-17 | 18/31 (SW 900, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.37×** | +6.7 | 3e-09 | 26/48 (HepG2/C3A, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.37×** | +6.6 | 3e-09 | 18/39 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +4.6 | 4e-04 | 14/48 (LoVo, HT-29, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.18× | +3.4 | 0.040 | 14/46 (CFPAC-1, A-427, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.065 | 8/44 (J82, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.33×** | +3.1 | 0.090 | 3/46 (A498, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | 1.16× | +3.1 | 0.090 | 6/47 (C-33 A, Hs 766T, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.0 | 0.11 | 11/48 (LoVo, A498, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3683.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.663×** | -8.7 | 2e-15 | 25/47 (A498, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.764×** | -7.7 | 4e-12 | 24/47 (H4, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.709×** | -7.3 | 7e-11 | 24/47 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.741×** | -6.4 | 3e-08 | 24/48 (A498, A-172, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.738×** | -6.2 | 8e-08 | 21/47 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.769×** | -5.1 | 3e-05 | 19/44 (SNU-1, NCI-H661, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Apalutamide (drug)]] 5 µM |  | 0.857× | -3.1 | 0.13 | 6/47 (CHP-212, LS 180, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3683. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 34.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.348× (z -11.0) |
| [[HS-578T (line)]] | alt | 28.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -13.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.334× (z -9.1) |
| [[SW480 (line)]] | alt | 14.2 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.07× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.149× (z -16.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 24.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -15.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H1792 (line)]] | alt | 22.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.229× (z -10.6) |
| [[NCI-H2347 (line)]] | alt | 18.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -9.0) ⚠ cell-cycle shift, explains ~28% of this change |
| [[RKO (line)]] | wt | 13.1 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0924× (z -11.0) |
| [[A-172 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3683), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAR1A]] | +0.75 | +0.81 / +0.65 | both halves | 7e-06 |  |
| [[CYB561D2]] | +0.72 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[PDIA4]] | +0.72 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[TM9SF2]] | +0.72 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[TMED9]] | +0.71 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[IER3IP1]] | +0.71 | +0.74 / +0.57 | both halves | 1e-05 |  |
| [[GPR107]] | +0.71 | +0.77 / +0.62 | both halves | 7e-06 |  |
| [[ADIPOR1]] | +0.71 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[YIPF2]] | +0.70 | +0.75 / +0.55 | both halves | 1e-05 |  |
| [[SKIC2]] | +0.70 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[NOMO2]] | +0.69 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[ORMDL3]] | +0.69 | +0.65 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC122]] | -0.62 | -0.58 / -0.37 | both halves | 8e-05 |  |
| [[INO80D]] | -0.61 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[PBDC1]] | -0.61 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[THOC7]] | -0.61 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[WARS2-AS1]] | -0.60 | -0.53 / -0.40 | both halves | 4e-05 |  |
| [[ST7L]] | -0.60 | -0.60 / -0.35 | both halves | 1e-04 |  |
| [[METTL18]] | -0.59 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[KRCC1]] | -0.59 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[MED13]] | -0.59 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[NEPRO-AS1]] | -0.59 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[MZF1-AS1]] | -0.59 | -0.56 / -0.31 | both halves | 2e-04 |  |
| [[TRIM47]] | -0.58 | -0.53 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers GGCX's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.774). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.2, -31.1); signed map (-53.0, 6.0). **Vector** length 80.8, 14.4% of its response variance represented; |z| ≥ 3 in 958 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *UPR ER* (control, mean cos +0.57 to 11); *Maturation of DENV proteins* (reactome, mean cos +0.51 to 11); *Dengue Virus Genome Translation and Replication* (reactome, mean cos +0.51 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +4.2 | +15.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.8 | +17.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +6.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.3 | +13.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +8.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +4.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +0.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.4 | +2.8 |
|  | [[Lipoic acid (drug)]] 5 µM |  | +1.2 | +1.3 |
|  | [[Lopinavir (drug)]] 5 µM |  | +1.1 | +2.2 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.8 | -6.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -5.7 | -7.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.1 | -7.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.9 | -8.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -6.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.5 | -5.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.9 | -1.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.9 | -2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.8 | +1.9 |

## What is on record

|  |  |
|---|---|
| Name | gamma-glutamyl carboxylase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p11.2 — chr2:85,544,720-85,561,532 (-) |
| Ensembl biotype | protein_coding |
| Also known as | VKCFD1 |
| Reactome | 6 pathways, smallest: Defective factor IX causes hemophilia B; Gamma-carboxylation of protein precursors; Gamma-carboxylation, transport, and amino-terminal cleavage of proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [P38435](https://www.uniprot.org/uniprotkb/P38435) (Vitamin K-dependent gamma-carboxylase):

> Mediates the vitamin K-dependent carboxylation of glutamate residues to calcium-binding gamma-carboxyglutamate (Gla) residues with the concomitant epoxidation of vitamin K hydroquinone to vitamin K epoxide. Couples epoxidation and carboxylation in the same active site. Catalyzes gamma-carboxylation of blood coagulation factors (F2, F7, F9 and F10) and anticoagulants such as PROC, which are essential for thrombosis. Catalyzes gamma-carboxylation of osteocalcin/BGLAP, which is essential for bone …

**Summary**, from NCBI Gene [2677](https://www.ncbi.nlm.nih.gov/gene/2677):

> This gene encodes an integral membrane protein of the rough endoplasmic reticulum that carboxylates glutamate residues of vitamin K-dependent proteins to gamma carboxyl glutamate, a modification that is required for their activity. The vitamin K-dependent protein substrates have a propeptide that binds the enzyme, with carbon dioxide, dioxide, and reduced vitamin K acting as co-substrates. Vitamin K-dependent proteins affect a number of physiologic processes including blood coagulation, …

**Accessions** — [HGNC:4247](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4247) · Entrez [2677](https://www.ncbi.nlm.nih.gov/gene/2677) · UniProt [P38435](https://www.uniprot.org/uniprotkb/P38435) · Ensembl [ENSG00000115486](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115486)

## Data

Gene col 3683: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3683); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3683, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3683]; `tensor/DDL_lfc|DDL_z.npy` [3683]; `embed/gene_vectors.npy` [3683]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3683 or target_col == 3683). Every well: [[GGCX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GGCX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
