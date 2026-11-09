---
symbol: "USP19"
type: "gene"
col: 10203
ensembl_id: "ENSG00000172046"
name: "ubiquitin specific peptidase 19"
location: "3p21.31"
module: 138
arm: "+"
pooled_cpm: 10.37
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 6
n_dd_up_clean: 3
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/138"]
generated_by: "tahoemap"
---

# USP19

*ubiquitin specific peptidase 19* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.61× (z +8.5, q 7e-15, up in 31 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.652× (z -7.7, q 9e-12, down in 31 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP13A1]] (+0.74, fdr 7e-06), [[TAOK2]] (+0.72, fdr 7e-06), [[STRN4]] (+0.71, fdr 7e-06); moves opposite to [[DPM1]] (-0.53, fdr 4e-05).
> It is in [[Module 138]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → cells under [[Fluvoxamine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10203.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.61×** | +8.5 | 7e-15 | 31/45 (LOX-IMVI, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.44×** | +4.7 | 9e-04 | 21/47 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.39×** | +4.2 | 0.004 | 15/42 (HOP62, AsPC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +4.2 | 0.004 | 18/43 (NCI-H1573, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.25×** | +4.0 | 0.006 | 17/48 (NCI-H1573, Panc 03.27, …) | top dose only | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +3.5 | 0.046 | 6/19 (SW480, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 1.28× | +3.1 | 0.17 | 14/46 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10203.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.652×** | -7.7 | 9e-12 | 31/46 (NCI-H23, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.747×** | -5.2 | 5e-05 | 24/48 (SW1417, SHP-77, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.694×** | -4.6 | 6e-04 | 21/46 (CFPAC-1, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | **0.810×** | -3.8 | 0.021 | 19/47 (Hs 766T, H4, …) | rises with dose | position effect removed |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | **0.759×** | -3.5 | 0.050 | 14/47 (SK-MEL-2, A-172, …) | inconsistent across doses | position effect removed |
| [[Bendamustine (drug)]] 5 µM |  | **0.755×** | -3.4 | 0.056 | 13/46 (C-33 A, SHP-77, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 0.780× | -3.0 | 0.19 | 13/45 (SK-MEL-2, A-427, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10203. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 20.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -9.4) |
| [[SW48 (line)]] | wt | 17.7 | 0 | 2 | — | [[Bosentan (hydrate) (drug)]] 0.05 µM 0.0834× (z -9.8) |
| [[A-172 (line)]] | wt | 8.64 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0662× (z -13.1) |
| [[CFPAC-1 (line)]] | alt | 5.29 | 0 | 1 | — | [[Tucidinostat (drug)]] 0.5 µM 0.0447× (z -13.7) |
| [[HEC-1-A (line)]] | alt | 12.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.227× (z -8.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 7.22 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.105× (z -10.0) |
| [[LOX-IMVI (line)]] | wt | 10.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +8.6) | — |
| [[NCI-H23 (line)]] | alt | 13.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -11.5) |
| [[SNU-1 (line)]] | wt | 8.94 | 0 | 1 | — | [[Furosemide (drug)]] 0.05 µM 0.0859× (z -8.6) |
| [[A-427 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.27 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.62 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.90 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.03 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.05 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.97 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.76 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.61 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10203), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP13A1]] | +0.74 | +0.66 / +0.78 | both halves | 7e-06 |  |
| [[TAOK2]] | +0.72 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[STRN4]] | +0.71 | +0.74 / +0.77 | both halves | 7e-06 |  |
| [[CNOT3]] | +0.70 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[PIGO]] | +0.69 | +0.55 / +0.72 | both halves | 1e-05 |  |
| [[MED16]] | +0.69 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[WASH8P]] ⚠ | +0.68 | +0.52 / +0.79 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[WDR6]] | +0.68 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[BAP1]] | +0.68 | +0.50 / +0.76 | both halves | 1e-05 | pathway: Deubiquitination |
| [[PRPF31]] | +0.67 | +0.54 / +0.76 | both halves | 1e-05 |  |
| [[GIGYF1]] | +0.67 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[MED12]] | +0.66 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[WIZ]] | +0.66 | +0.65 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPM1]] | -0.53 | -0.42 / -0.52 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Fluvoxamine (drug)]] 0.5 µM | C | USP19's natural level raises the cells' numbers under Fluvoxamine 0.5 µM (protects the cells) | USP19's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.58 | 0.491 over the table, 0.094 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Clofarabine (drug)]] 0.5 µM | C | USP19's natural level raises the cells' numbers under Clofarabine 0.5 µM (protects the cells) | USP19's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.57 | 0.511 over the table, 0.088 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 138]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.779). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.8, -23.8); signed map (-10.8, -32.1). **Vector** length 70.7, 11.2% of its response variance represented; |z| ≥ 3 in 898 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +4.7 | +4.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.3 | +8.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +3.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.8 | +1.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +2.7 | +4.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +2.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +1.1 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.7 | +2.3 |
|  | [[Arbutin (drug)]] 0.5 µM |  | +1.6 | +2.0 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.5 | +3.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -5.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.4 | -7.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -3.2 | -2.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -3.2 | -3.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.2 | -4.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.2 | -0.9 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -2.0 | -3.5 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.5 | -1.8 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -1.5 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin specific peptidase 19 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:49,108,046-49,120,938 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0891, ZMYND9 |
| Gene groups (HGNC) | Zinc fingers MYND-type; Ubiquitin specific peptidases |
| Reactome | 2 pathways, smallest: Ub-specific processing proteases; Deubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [O94966](https://www.uniprot.org/uniprotkb/O94966) (Ubiquitin carboxyl-terminal hydrolase 19):

> Deubiquitinating enzyme that regulates the degradation of various proteins by removing ubiquitin moieties, thereby preventing their proteasomal degradation. Stabilizes RNF123, which promotes CDKN1B degradation and contributes to cell proliferation (By similarity). Decreases the levels of ubiquitinated proteins during skeletal muscle formation and acts to repress myogenesis. Modulates transcription of major myofibrillar proteins. Also involved in turnover of endoplasmic-reticulum-associated …

**Summary**, from NCBI Gene [10869](https://www.ncbi.nlm.nih.gov/gene/10869):

> Protein ubiquitination controls many intracellular processes, including cell cycle progression, transcriptional activation, and signal transduction. This dynamic process, involving ubiquitin conjugating enzymes and deubiquitinating enzymes, adds and removes ubiquitin. Deubiquitinating enzymes are cysteine proteases that specifically cleave ubiquitin from ubiquitin-conjugated protein substrates. This protein is a ubiquitin protein ligase and plays a role in muscle wasting. Alternatively spliced …

**Accessions** — [HGNC:12617](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12617) · Entrez [10869](https://www.ncbi.nlm.nih.gov/gene/10869) · UniProt [O94966](https://www.uniprot.org/uniprotkb/O94966) · Ensembl [ENSG00000172046](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172046)

## Data

Gene col 10203: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10203); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10203, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10203]; `tensor/DDL_lfc|DDL_z.npy` [10203]; `embed/gene_vectors.npy` [10203]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10203 or target_col == 10203). Every well: [[USP19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
