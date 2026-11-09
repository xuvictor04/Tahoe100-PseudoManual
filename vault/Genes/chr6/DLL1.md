---
symbol: "DLL1"
type: "gene"
col: 12651
ensembl_id: "ENSG00000198719"
name: "delta like canonical Notch ligand 1"
location: "6q27"
module: 35
arm: "+"
pooled_cpm: 3.58
n_lines_expressing: 48
n_dd_up: 29
n_dd_down: 0
n_dd_up_clean: 24
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# DLL1

*delta like canonical Notch ligand 1* — 6q27

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.12× (z +23.8, q 0e+00, up in 31 of 32 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (LoVo 0.0892×); [[Harringtonine (drug)]] 0.05 µM in 1 line (RKO 0.0917×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAXBP1-AS1]] (+0.70, fdr 7e-06), [[ZC2HC1C]] (+0.67, fdr 8e-06), [[RETREG1-AS1]] (+0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 035]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12651.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.12×** | +23.8 | 0e+00 | 31/32 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.34×** | +14.3 | 8e-44 | 26/33 (hTERT-HPNE, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.23×** | +12.9 | 1e-35 | 4/7 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.62×** | +11.0 | 6e-26 | 1/4 (SNU-423) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.16×** | +9.1 | 8e-18 | 18/40 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.69×** | +8.8 | 1e-16 | 20/44 (SNU-423, PANC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.05×** | +8.5 | 2e-15 | 21/41 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.04×** | +8.5 | 2e-15 | 21/45 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.90×** | +7.6 | 2e-12 | 16/43 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.83×** | +7.2 | 5e-11 | 3/14 (SW480, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +6.7 | 1e-09 | 15/30 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +6.1 | 4e-08 | 7/18 (RPMI-7951, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.63×** | +6.0 | 9e-08 | 13/36 (NCI-H1573, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.57×** | +5.1 | 1e-05 | 14/40 (RPMI-7951, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.52×** | +4.9 | 3e-05 | 9/43 (LS 180, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.52×** | +4.6 | 1e-04 | 8/31 (NCI-H1573, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +4.5 | 3e-04 | 9/42 (SW1417, A-427, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.44×** | +4.3 | 5e-04 | 5/45 (PANC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.45×** | +4.1 | 0.001 | 4/38 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12651.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (LoVo 0.0892×); [[Harringtonine (drug)]] 0.05 µM in 1 line (RKO 0.0917×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | 0.743× | -3.5 | 0.24 | 9/42 (A-172, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 5 µM |  | 0.759× | -3.1 | 0.47 | 7/41 (Hs 766T, A549, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12651. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 3.43 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.64× (z +8.5) | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0892× (z -8.9) |
| [[A549 (line)]] | wt | 1.43 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.6× (z +9.8) | — |
| [[HEC-1-A (line)]] | alt | 2.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.96× (z +8.5) | — |
| [[hTERT-HPNE (line)]] | wt | 2.51 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.0× (z +8.7) | — |
| [[NCI-H460 (line)]] | wt | 1.42 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.1× (z +10.2) | — |
| [[PANC-1 (line)]] | alt | 4.45 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.79× (z +10.6) | — |
| [[RKO (line)]] | wt | 8.85 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0917× (z -8.8) |
| [[SW480 (line)]] | alt | 3.80 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.06× (z +10.7) | — |
| [[A-172 (line)]] | wt | 6.83 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.69 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.543 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.707 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.03 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.98 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12651), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAXBP1-AS1]] | +0.70 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[ZC2HC1C]] | +0.67 | +0.64 / +0.58 | both halves | 8e-06 |  |
| [[RETREG1-AS1]] | +0.64 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[MALINC1]] | +0.64 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[UPK2]] | +0.64 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[CHMP3-AS1]] | +0.63 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[UNC79]] | +0.63 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[NDUFV2-AS1]] | +0.61 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[C11orf71]] | +0.61 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[CNTNAP5]] | +0.60 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[CLVS1]] | +0.60 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[SEC1P]] | +0.60 | +0.55 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.628). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (8.9, 24.0); signed map (31.5, -3.2). **Vector** length 49.7, 6.33% of its response variance represented; |z| ≥ 3 in 980 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +23.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +11.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.5 | +14.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +12.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +7.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +8.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +3.7 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.6 | +1.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +4.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.2 | -1.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.6 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -1.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -1.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -2.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.1 | -1.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | delta like canonical Notch ligand 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q27 — chr6:170,282,206-170,306,565 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Canonical Notch ligands |
| Hallmark sets | NOTCH_SIGNALING, WNT_BETA_CATENIN_SIGNALING |
| Reactome | 28 pathways, smallest: Constitutive Signaling by NOTCH1 t(7;9)(NOTCH1:M1580_K2555) Translocation Mutant; MECP2 regulates transcription of neuronal ligands; Signaling by NOTCH1 t(7;9)(NOTCH1:M1580_K2555) Translocation Mutant |
| Matched by | ensembl_id |

**Function**, from UniProt [O00548](https://www.uniprot.org/uniprotkb/O00548) (Delta-like protein 1):

> Transmembrane ligand protein of NOTCH1, NOTCH2 and NOTCH3 receptors that binds the extracellular domain (ECD) of Notch receptor in a cis and trans fashion manner. Following transinteraction, ligand cells produce mechanical force that depends of a clathrin-mediated endocytosis, requiring ligand ubiquitination, EPN1 interaction, and actin polymerization; these events promote Notch receptor extracellular domain (NECD) transendocytosis and triggers Notch signaling through induction of cleavage, …

**Summary**, from NCBI Gene [28514](https://www.ncbi.nlm.nih.gov/gene/28514):

> DLL1 is a human homolog of the Notch Delta ligand and is a member of the delta/serrate/jagged family. It plays a role in mediating cell fate decisions during hematopoiesis. It may play a role in cell-to-cell communication. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2908](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2908) · Entrez [28514](https://www.ncbi.nlm.nih.gov/gene/28514) · UniProt [O00548](https://www.uniprot.org/uniprotkb/O00548) · Ensembl [ENSG00000198719](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198719)

## Data

Gene col 12651: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12651); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12651, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12651]; `tensor/DDL_lfc|DDL_z.npy` [12651]; `embed/gene_vectors.npy` [12651]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12651 or target_col == 12651). Every well: [[DLL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DLL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
