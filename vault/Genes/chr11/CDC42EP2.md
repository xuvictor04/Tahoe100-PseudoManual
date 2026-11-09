---
symbol: "CDC42EP2"
type: "gene"
col: 7410
ensembl_id: "ENSG00000149798"
name: "CDC42 effector protein 2"
location: "11q13.1"
module: 78
arm: "+"
pooled_cpm: 2.19
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 6
n_dd_up_clean: 5
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# CDC42EP2

*CDC42 effector protein 2* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.69× (z +5.3, q 6e-05, up in 8 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM: 0.528× (z -4.3, q 0.006, down in 10 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NES]] (+0.64, fdr 1e-05), [[ACTN1]] (+0.64, fdr 7e-06), [[NT5E]] (+0.61, fdr 1e-05); moves opposite to [[ANAPC16]] (-0.63, fdr 7e-06), [[TRPM7]] (-0.60, fdr 1e-05), [[ATP5MC2]] (-0.57, fdr 1e-05).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CD59]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7410.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.69×** | +5.3 | 6e-05 | 8/29 (PANC-1, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.17×** | +5.1 | 1e-04 | 1/7 (PANC-1) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.02×** | +5.0 | 1e-04 | 12/42 (SW480, LoVo, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.04×** | +4.8 | 2e-04 | 0/5 | all doses, flat | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.84×** | +4.3 | 0.002 | 13/39 (SW480, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.53×** | +4.3 | 0.002 | 7/29 (LoVo, SW480, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.86×** | +4.2 | 0.003 | 1/13 (BT-474) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +3.7 | 0.018 | 10/38 (NCI-H460, KATO III, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.63×** | +3.6 | 0.019 | 10/32 (J82, SW1417, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.43×** | +3.6 | 0.020 | 7/39 (SW480, NCI-H1792, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.65×** | +3.4 | 0.040 | 9/34 (HS-578T, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.57×** | +3.2 | 0.060 | 7/37 (SW480, MIA PaCa-2, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7410.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.528×** | -4.3 | 0.006 | 10/42 (Hs 766T, PANC-1, …) | all doses, flat | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.552×** | -4.2 | 0.006 | 14/42 (KATO III, HOP62, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **0.669×** | -4.1 | 0.009 | 9/37 (LS 180, HCT15, …) | top dose only |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.05 µM |  | **0.564×** | -3.8 | 0.023 | 8/37 (A549, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.660×** | -3.6 | 0.040 | 14/37 (Hs 766T, HCT15, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **0.713×** | -3.5 | 0.049 | 11/43 (Hs 766T, HT-29, …) | all doses, flat | noisy plate (z scaled) |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 0.730× | -3.2 | 0.12 | 11/38 (A-427, LS 180, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM |  | 0.713× | -3.1 | 0.12 | 9/42 (Hs 766T, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~7% here); noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7410. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.523 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.892 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.64 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.807 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.745 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.843 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.00 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.941 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7410), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NES]] | +0.64 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[ACTN1]] | +0.64 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[NT5E]] | +0.61 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[MAP4K4]] | +0.60 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[HAS3]] | +0.60 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[MICAL2]] | +0.59 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[SPRY4]] | +0.59 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[FURIN]] | +0.59 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[CD59]] | +0.59 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[PLXNA1]] | +0.58 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[F2RL1]] | +0.57 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[LRWD1]] | +0.57 | +0.58 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANAPC16]] | -0.63 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[TRPM7]] | -0.60 | -0.66 / -0.51 | both halves | 1e-05 |  |
| [[ATP5MC2]] | -0.57 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[SOS1]] | -0.56 | -0.54 / -0.59 | both halves | 1e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[KIF13A]] | -0.56 | -0.46 / -0.59 | both halves | 2e-05 |  |
| [[CAPN7]] | -0.56 | -0.54 / -0.65 | both halves | 1e-05 |  |
| [[UBE4B]] | -0.55 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[TUT4]] | -0.54 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[KIZ-AS1]] ⚠ | -0.54 | -0.48 / -0.49 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ABHD18]] | -0.54 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[FBXO42]] | -0.53 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[KIZ]] | -0.53 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[CNNM2]] | -0.53 | -0.51 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD59]] | B | CD59 activity raises CDC42EP2's level | lines that do not express CD59 (7) vs lines expressing it (43) | 1.45× lower at baseline in the lines without CD59 | 0.060 | ⚠ within organs, on part of the lines; also absent: C11orf91, ENSG00000284969, MET; maybe low, not absent |
| [[MAP2K2]] | B | MAP2K2 activity raises CDC42EP2's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.697). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.1, 5.8); signed map (6.9, 45.4). **Vector** length 55.4, 8.46% of its response variance represented; |z| ≥ 3 in 976 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +5.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +4.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.3 | +0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +3.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +1.9 | +4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +3.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.3 | +1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +0.2 |
|  | [[Ivermectin (drug)]] 0.5 µM |  | +1.1 | +2.2 |
| fall | [[Trametinib (drug)]] 5 µM |  | -2.6 | -3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.6 | -4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.2 | -4.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.1 | -3.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.1 | -2.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.1 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | CDC42 effector protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:65,314,866-65,322,417 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CEP2, BORG1 |
| Gene groups (HGNC) | CDC42 effector proteins |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 7 pathways, smallest: RHOQ GTPase cycle; MAPK6/MAPK4 signaling; CDC42 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [O14613](https://www.uniprot.org/uniprotkb/O14613) (Cdc42 effector protein 2):

> Probably involved in the organization of the actin cytoskeleton. May act downstream of CDC42 to induce actin filament assembly leading to cell shape changes. Induces pseudopodia formation in fibroblasts in a CDC42-dependent manner.

**Summary**, from NCBI Gene [10435](https://www.ncbi.nlm.nih.gov/gene/10435):

> CDC42, a small Rho GTPase, regulates the formation of F-actin-containing structures through its interaction with the downstream effector proteins. The protein encoded by this gene is a member of the Borg family of CDC42 effector proteins. Borg family proteins contain a CRIB (Cdc42/Rac interactive-binding) domain. They bind to, and negatively regulate the function of CDC42. Coexpression of this protein with CDC42 suggested a role of this protein in actin filament assembly and cell shape control. …

**Accessions** — [HGNC:16263](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16263) · Entrez [10435](https://www.ncbi.nlm.nih.gov/gene/10435) · UniProt [O14613](https://www.uniprot.org/uniprotkb/O14613) · Ensembl [ENSG00000149798](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149798)

## Data

Gene col 7410: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7410); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7410, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7410]; `tensor/DDL_lfc|DDL_z.npy` [7410]; `embed/gene_vectors.npy` [7410]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7410 or target_col == 7410). Every well: [[CDC42EP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDC42EP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
