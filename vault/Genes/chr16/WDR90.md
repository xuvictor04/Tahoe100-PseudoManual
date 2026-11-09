---
symbol: "WDR90"
type: "gene"
col: 8469
ensembl_id: "ENSG00000161996"
name: "WD repeat domain 90"
location: "16p13.3"
module: 6
arm: "+"
pooled_cpm: 7.26
n_lines_expressing: 48
n_dd_up: 13
n_dd_down: 6
n_dd_up_clean: 2
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# WDR90

*WD repeat domain 90* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 2.04× (z +7.6, q 2e-11, up in 14 of 24 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 1.44× (z +4.1, q 0.003, up in 15 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.588× (z -8.7, q 2e-15, down in 32 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RECQL4]] (+0.73, fdr 7e-06), [[PKMYT1]] (+0.73, fdr 7e-06), [[POLE]] (+0.73, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 11 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8469.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.04×** | +7.6 | 2e-11 | 14/24 (PANC-1, SW480, …) | all doses, flat | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.89×** | +7.1 | 5e-10 | 9/15 (SW480, SW1417, …) | all doses, flat | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **1.87×** | +6.9 | 8e-10 | 16/33 (LS 180, SK-MEL-2, …) | all doses, flat | composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.59×** | +5.1 | 4e-05 | 19/41 (LOX-IMVI, NCI-H460, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.34×** | +4.7 | 3e-04 | 19/41 (NCI-H2030, NCI-H2347, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.47×** | +4.5 | 8e-04 | 17/45 (KATO III, A-427, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.43×** | +4.1 | 0.003 | 15/43 (AsPC-1, KATO III, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.44×** | +4.1 | 0.003 | 15/42 (PANC-1, AsPC-1, …) | top dose only | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.27×** | +4.0 | 0.005 | 17/40 (PANC-1, NCI-H2030, …) | top dose only | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.38×** | +3.8 | 0.010 | 12/45 (NCI-H460, RKO, …) | inconsistent across doses | position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +3.6 | 0.019 | 5/21 (SK-MEL-2, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.36×** | +3.3 | 0.047 | 11/39 (NCI-H2030, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.34×** | +3.2 | 0.052 | 11/44 (J82, NCI-H460, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.30× | +3.0 | 0.11 | 7/46 (SK-MEL-2, COLO 205, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8469.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.588×** | -8.7 | 2e-15 | 32/46 (SW480, J82, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.491×** | -8.2 | 5e-14 | 30/43 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.508×** | -4.1 | 0.008 | 8/44 (SK-MEL-2, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.801×** | -3.6 | 0.038 | 9/46 (hTERT-HPNE, SHP-77, …) | rises with dose | position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.738×** | -3.5 | 0.048 | 14/45 (A-427, LOX-IMVI, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.581×** | -3.3 | 0.096 | 7/41 (NCI-H23, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 0.825× | -3.2 | 0.10 | 13/46 (KATO III, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 0.764× | -3.1 | 0.10 | 15/44 (A498, RKO, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.765× | -3.1 | 0.10 | 11/45 (Hs 766T, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.828× | -3.1 | 0.10 | 12/46 (A-427, LS 180, …) | rises with dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 0.766× | -3.1 | 0.10 | 12/43 (SNU-1, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.50 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8469. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 11.6 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.168× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 11.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[SNU-423 (line)]] | alt | 5.05 | 0 | 1 | — | [[Macitentan (drug)]] 5 µM 0.0974× (z -9.1) |
| [[A-427 (line)]] | wt | 9.44 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.47 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.14 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.61 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.05 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.25 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.40 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.51 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8469), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RECQL4]] | +0.73 | +0.71 / +0.79 | both halves | 7e-06 |  |
| [[PKMYT1]] | +0.73 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[POLE]] | +0.73 | +0.70 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[TONSL]] | +0.73 | +0.65 / +0.77 | both halves | 7e-06 | STRING 515 |
| [[E2F1]] | +0.70 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[CHAF1A]] | +0.69 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[XRCC3]] | +0.68 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[MCM5]] | +0.68 | +0.62 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[PASK]] | +0.68 | +0.61 / +0.64 | both halves | 7e-06 | STRING 414 |
| [[MCM2]] | +0.68 | +0.65 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[MCM7]] | +0.67 | +0.66 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[CENPM]] | +0.66 | +0.64 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.628). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-35.4, -43.3); signed map (-36.7, -46.1). **Vector** length 77.4, 14.4% of its response variance represented; |z| ≥ 3 in 824 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.53 to 28); *DNA Replication* (reactome, mean cos +0.52 to 40); *E2F G1/S* (control, mean cos +0.54 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | +3.0 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | +2.8 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +2.6 | +7.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +2.5 | +5.1 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +2.5 | +3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +2.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.9 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +1.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.8 | +1.3 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.5 | +1.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.7 | -8.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.2 | -8.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -2.6 | -3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -3.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.4 | -3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | -3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.0 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 90 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:649,311-667,833 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ36483, KIAA1924, POC16; previously C16orf17, C16orf15, C16orf16, C16orf19, C16orf18 |
| Gene groups (HGNC) | WD repeat domain containing |
| Hallmark sets | E2F_TARGETS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96KV7](https://www.uniprot.org/uniprotkb/Q96KV7) (WD repeat-containing protein 90):

> Microtubule-binding protein that plays a crucial role in ensuring inner core protein localization within the centriole core, as well as in maintaining the microtubule wall integrity and the overall centriole roundness and stability. Required for efficient primary cilium formation.

**Summary**, from NCBI Gene [197335](https://www.ncbi.nlm.nih.gov/gene/197335):

> Enables microtubule binding activity. Involved in centriole elongation and cilium assembly. Located in centriolar satellite; centriole; and ciliary basal body. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26960](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26960) · Entrez [197335](https://www.ncbi.nlm.nih.gov/gene/197335) · UniProt [Q96KV7](https://www.uniprot.org/uniprotkb/Q96KV7) · Ensembl [ENSG00000161996](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161996)

## Data

Gene col 8469: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8469); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8469, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8469]; `tensor/DDL_lfc|DDL_z.npy` [8469]; `embed/gene_vectors.npy` [8469]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8469 or target_col == 8469). Every well: [[WDR90 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR90.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
