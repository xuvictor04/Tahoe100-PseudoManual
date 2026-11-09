---
symbol: "EIF2S2"
type: "gene"
col: 4703
ensembl_id: "ENSG00000125977"
name: "eukaryotic translation initiation factor 2 subunit beta"
location: "20q11.22"
module: 63
arm: "+"
pooled_cpm: 208.65
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 5
n_dd_up_clean: 4
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# EIF2S2

*eukaryotic translation initiation factor 2 subunit beta* — 20q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.71× (z +5.0, q 4e-04, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.534× (z -5.7, q 6e-06, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CARS1]] (+0.82, fdr 7e-06), [[GARS1]] (+0.81, fdr 7e-06), [[SARS1]] (+0.80, fdr 7e-06); moves opposite to [[TAGLN2]] (-0.53, fdr 3e-05), [[TGOLN2]] (-0.51, fdr 3e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GDF15]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4703.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.71×** | +5.0 | 4e-04 | 44/48 (C32, AsPC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.94×** | +4.5 | 0.002 | 38/49 (A549, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +4.4 | 0.002 | 37/47 (AsPC-1, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +4.1 | 0.005 | 31/44 (A549, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.53×** | +3.9 | 0.009 | 44/48 (NCI-H2030, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.030 | 38/48 (SNU-1, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.049 | 37/49 (CHP-212, SW 900, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.39× | +3.1 | 0.15 | 36/48 (NCI-H2030, C-33 A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4703.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.534×** | -5.7 | 6e-06 | 46/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.664×** | -5.3 | 4e-05 | 35/48 (HT-29, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.617×** | -4.4 | 0.002 | 42/48 (PANC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.655×** | -3.8 | 0.017 | 42/48 (PANC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.689×** | -3.4 | 0.083 | 34/48 (KATO III, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4703. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 279 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -11.0) |
| [[HT-29 (line)]] | alt | 380 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -12.4) |
| [[A-427 (line)]] | wt | 272 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -10.8) |
| [[A549 (line)]] | wt | 134 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.47× (z +8.9) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 142 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -14.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 88.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.41× (z +10.2) | — |
| [[H4 (line)]] | wt | 183 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.108× (z -8.5) ⚠ toxic |
| [[KATO III (line)]] | alt | 415 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -8.6) |
| [[RKO (line)]] | wt | 318 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -9.9) |
| [[SNU-1 (line)]] | wt | 267 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -10.4) |
| [[SW1417 (line)]] | alt | 356 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.476× (z -9.4) |
| [[SW48 (line)]] | wt | 207 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -9.1) |
| [[A-172 (line)]] | wt | 192 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 260 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 109 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 128 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 177 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 111 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 234 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 356 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 205 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 131 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 237 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 209 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 175 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 203 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 213 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 187 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 231 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 194 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 157 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 229 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 202 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 196 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 450 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 247 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4703), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CARS1]] | +0.82 | +0.80 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[GARS1]] | +0.81 | +0.76 / +0.81 | both halves | 7e-06 |  |
| [[SARS1]] | +0.80 | +0.79 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[CEBPG]] | +0.79 | +0.84 / +0.71 | both halves | 7e-06 | pathway: Cellular response to starvation; STRING 567 |
| [[TRIB3]] | +0.78 | +0.70 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[AARS1]] | +0.76 | +0.79 / +0.74 | both halves | 7e-06 | STRING 494 |
| [[SESN2]] | +0.76 | +0.72 / +0.78 | both halves | 7e-06 | pathway: Cellular response to starvation |
| [[XPOT]] | +0.76 | +0.80 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[MARS1]] | +0.76 | +0.80 / +0.71 | both halves | 7e-06 | STRING 597 |
| [[DMGDH]] | +0.74 | +0.69 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[YARS1]] | +0.74 | +0.79 / +0.68 | both halves | 7e-06 | STRING 610 |
| [[ASNS]] | +0.73 | +0.77 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 587 |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAGLN2]] | -0.53 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[TGOLN2]] | -0.51 | -0.43 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GDF15]] | B | GDF15 activity lowers EIF2S2's level | lines that do not express GDF15 (18) vs lines expressing it (32) | 1.06× higher at baseline in the lines without GDF15 | 0.041 | ⚠ within organs, on part of the lines; also absent: PCSK5, ALOX5, LINC03040 |
| [[HDAC6]] | B | HDAC6 activity raises EIF2S2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.806). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.6, 48.1); signed map (-12.8, 24.0). **Vector** length 111, 52.7% of its response variance represented; |z| ≥ 3 in 721 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ISR ATF4* (control, mean cos +0.67 to 16); *Cytosolic tRNA aminoacylation* (reactome, mean cos +0.74 to 9); *tRNA Aminoacylation* (reactome, mean cos +0.74 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[5-Azacytidine (drug)]] 5 µM |  | +6.7 | +3.1 |
|  | [[Artesunate (drug)]] 5 µM |  | +5.7 | +3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.5 | +5.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.1 | +2.7 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM |  | +5.1 | +3.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +4.5 | +2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.4 | +3.4 |
|  | [[Neratinib (drug)]] 5 µM |  | +3.9 | +2.7 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.2 | +2.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.9 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.7 | +4.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.4 | -1.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.1 | -3.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.7 | -1.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.3 | -2.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.9 | -0.9 |
|  | [[Adenine (drug)]] 5 µM |  | -1.8 | -1.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.7 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 2 subunit beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.22 — chr20:34,088,309-34,112,243 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EIF2beta, PPP1R67; previously EIF2 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits |
| Hallmark sets | MTORC1_SIGNALING, MYC_TARGETS_V1 |
| Reactome | 24 pathways, smallest: Recycling of eIF2:GDP; Cellular response to mitochondrial stress; Response of EIF2AK1 (HRI) to heme deficiency |
| Matched by | ensembl_id |

**Function**, from UniProt [P20042](https://www.uniprot.org/uniprotkb/P20042) (Eukaryotic translation initiation factor 2 subunit 2):

> Component of the eIF2 complex that functions in the early steps of protein synthesis by forming a ternary complex with GTP and initiator tRNA. This complex binds to a 40S ribosomal subunit, followed by mRNA binding to form the 43S pre-initiation complex (43S PIC). Junction of the 60S ribosomal subunit to form the 80S initiation complex is preceded by hydrolysis of the GTP bound to eIF2 and release of an eIF2-GDP binary complex. In order for eIF2 to recycle and catalyze another round of …

**Summary**, from NCBI Gene [8894](https://www.ncbi.nlm.nih.gov/gene/8894):

> Eukaryotic translation initiation factor 2 (EIF-2) functions in the early steps of protein synthesis by forming a ternary complex with GTP and initiator tRNA and binding to a 40S ribosomal subunit. EIF-2 is composed of three subunits, alpha, beta, and gamma, with the protein encoded by this gene representing the beta subunit. The beta subunit catalyzes the exchange of GDP for GTP, which recycles the EIF-2 complex for another round of initiation. Multiple transcript variants encoding different …

**Accessions** — [HGNC:3266](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3266) · Entrez [8894](https://www.ncbi.nlm.nih.gov/gene/8894) · UniProt [P20042](https://www.uniprot.org/uniprotkb/P20042) · Ensembl [ENSG00000125977](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125977)

## Data

Gene col 4703: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4703); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4703, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4703]; `tensor/DDL_lfc|DDL_z.npy` [4703]; `embed/gene_vectors.npy` [4703]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4703 or target_col == 4703). Every well: [[EIF2S2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF2S2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
