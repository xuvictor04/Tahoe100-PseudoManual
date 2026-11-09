---
symbol: "TERB1"
type: "gene"
col: 14655
ensembl_id: "ENSG00000249961"
name: "telomere repeat binding bouquet formation protein 1"
location: "16q22.1"
module: 39
arm: "+"
pooled_cpm: 2.27
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 8
n_dd_up_clean: 15
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# TERB1

*telomere repeat binding bouquet formation protein 1* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.22× (z +18.0, q 0e+00, up in 25 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.497× (z -6.2, q 3e-07, down in 17 of 45 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.546× (z -5.3, q 2e-05, down in 19 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDC20-DT]] (+0.75, fdr 7e-06), [[MSH4]] (+0.71, fdr 7e-06), [[CD200R1]] (+0.70, fdr 7e-06).
> It is in [[Module 039]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14655.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.22×** | +18.0 | 0e+00 | 25/26 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **6.30×** | +15.7 | 0e+00 | 7/8 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.44×** | +10.5 | 1e-23 | 14/23 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **2.19×** | +9.8 | 1e-20 | 24/43 (NCI-H2030, NCI-H460, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.86×** | +8.9 | 4e-17 | 1/3 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.41×** | +7.2 | 6e-11 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.29×** | +7.1 | 1e-10 | 13/30 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.54×** | +5.4 | 5e-06 | 9/41 (NCI-H460, SW480, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.09×** | +5.2 | 1e-05 | 3/3 (NCI-H2030, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.77×** | +5.0 | 3e-05 | 14/44 (RKO, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.72×** | +4.8 | 8e-05 | 10/34 (SW480, HOP62, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.63×** | +4.3 | 7e-04 | 9/46 (SW480, LoVo, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.61×** | +3.9 | 0.003 | 6/32 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.36×** | +3.9 | 0.004 | 5/27 (A498, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **2.13×** | +3.5 | 0.017 | 3/31 (NCI-H2030, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.49×** | +3.3 | 0.029 | 7/39 (BT-474, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.47×** | +3.2 | 0.038 | 3/20 (NCI-H2030, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.43×** | +3.2 | 0.045 | 4/35 (LS 180, A498, …) | inconsistent across doses |  |
| [[Terfenadine (drug)]] 5 µM |  | **1.27×** | +3.0 | 0.068 | 5/40 (A-427, PANC-1, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14655.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.497×** | -6.2 | 3e-07 | 17/45 (HepG2/C3A, HEC-1-A, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.546×** | -5.3 | 2e-05 | 19/41 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.550×** | -5.1 | 7e-05 | 17/39 (HOP62, Hs 766T, …) | rises with dose | composition shift |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.619×** | -4.1 | 0.006 | 8/19 (SW480, KATO III, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.666×** | -3.6 | 0.036 | 11/31 (NCI-H23, NCI-H2030, …) | all doses, flat |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.673×** | -3.4 | 0.069 | 5/44 (C-33 A, SK-MEL-2, …) | top dose only | plate-row cell shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.494×** | -3.3 | 0.083 | 9/23 (SW480, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.678×** | -3.2 | 0.083 | 8/26 (MIA PaCa-2, HOP62, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14655. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 2.50 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.91× (z +9.6) | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0834× (z -8.8) |
| [[A498 (line)]] | wt | 1.11 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.8× (z +9.9) | — |
| [[A549 (line)]] | wt | 2.41 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -8.5) |
| [[BT-474 (line)]] | alt | 8.89 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.0993× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 3.34 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.28× (z +8.7) | — |
| [[SW480 (line)]] | alt | 2.96 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 8.35× (z +8.5) ⚠ toxic | — |
| [[A-172 (line)]] | wt | 0.871 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.822 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.741 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.964 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.634 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.90 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14655), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC20-DT]] | +0.75 | +0.62 / +0.74 | both halves | 7e-06 |  |
| [[MSH4]] | +0.71 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[CD200R1]] | +0.70 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[BAAT]] | +0.69 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[ARL9]] | +0.69 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[LINC01030]] | +0.68 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[OOEP]] | +0.67 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[CCDC181]] | +0.67 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[PRC1-AS1]] | +0.66 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[GTF2IP5]] | +0.66 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[SPATA1]] | +0.65 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[TOMM20L-DT]] | +0.65 | +0.54 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.593). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.1, -14.7); signed map (15.9, 5.0). **Vector** length 54.1, 7.88% of its response variance represented; |z| ≥ 3 in 1,037 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +18.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.4 | +15.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.4 | +9.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +7.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.3 | +3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +5.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.6 | +3.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.5 | +4.3 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.9 | -6.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -0.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -5.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -1.9 | -5.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | +1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.7 | +0.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.4 | -2.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.2 | -2.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -2.0 |
|  | [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | -1.1 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | telomere repeat binding bouquet formation protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:66,754,640-66,801,620 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ35894; previously CCDC79 |
| Gene groups (HGNC) | Myb/SANT domain containing; Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NA31](https://www.uniprot.org/uniprotkb/Q8NA31) (Telomere repeats-binding bouquet formation protein 1):

> Meiosis-specific telomere-associated protein involved in meiotic telomere attachment to the nucleus inner membrane, a crucial step for homologous pairing and synapsis. Component of the MAJIN-TERB1-TERB2 complex, which promotes telomere cap exchange by mediating attachment of telomeric DNA to the inner nuclear membrane and replacement of the protective cap of telomeric chromosomes: in early meiosis, the MAJIN-TERB1-TERB2 complex associates with telomeric DNA and the shelterin/telosome complex. …

**Summary**, from NCBI Gene [283847](https://www.ncbi.nlm.nih.gov/gene/283847):

> Predicted to be involved in homologous chromosome pairing at meiosis and meiotic attachment of telomere to nuclear envelope. Predicted to act upstream of or within double-strand break repair involved in meiotic recombination. Located in nuclear envelope. Implicated in spermatogenic failure 60. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26675](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26675) · Entrez [283847](https://www.ncbi.nlm.nih.gov/gene/283847) · UniProt [Q8NA31](https://www.uniprot.org/uniprotkb/Q8NA31) · Ensembl [ENSG00000249961](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000249961)

## Data

Gene col 14655: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14655); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14655, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14655]; `tensor/DDL_lfc|DDL_z.npy` [14655]; `embed/gene_vectors.npy` [14655]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14655 or target_col == 14655). Every well: [[TERB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TERB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
